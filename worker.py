import requests
import os
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods

# --- Watsonx LLM Configuration ---
# Note: PROJECT_ID="skills-network" is specific to the Cloud IDE environment.
PROJECT_ID = "skills-network"
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
}

# Specify the model ID
model_id = "mistralai/mistral-medium-2505"

# Define the model parameters
parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 1024
}

# Initialize the Model
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=PROJECT_ID
)

def watsonx_process_message(user_message):
    """
    Sends the user message to Watsonx for translation.
    """
    prompt = f"""
    Translate the following English sentence into Spanish. 
    Reply ONLY with the translation, no explanations, no formatting, no extra text.
    English: {user_message}
    Spanish:
    """
    response_text = model.generate_text(prompt=prompt)
    print("watsonx response:", response_text)
    return response_text.strip()

def speech_to_text(audio_binary):
    """
    Converts audio binary data to text using Watson Speech-to-Text.
    """
    # Replace with the endpoint provided in your environment
    base_url = 'https://sn-watson-stt.labs.skills.network'
    api_url = base_url + '/speech-to-text/api/v1/recognize'
    
    params = {
        'model': 'en-US_Multimedia',
    }
    
    # Send the POST request with the audio binary
    response = requests.post(api_url, params=params, data=audio_binary).json()
    
    text = 'null'
    if response.get('results'):
        print('Speech-to-Text response:', response)
        # Extract the transcript from the results
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('Recognized text:', text)
        
    return text

def text_to_speech(text, voice=""):
    """
    Converts text to audio data using Watson Text-to-Speech.
    """
    # Replace with the endpoint provided in your environment
    base_url = 'https://sn-watson-tts.labs.skills.network'
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'
    
    # Add voice parameter if selected
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice
        
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }
    
    json_data = {
        'text': text,
    }
    
    # Send the POST request to synthesize speech
    response = requests.post(api_url, headers=headers, json=json_data)
    print('Text-to-Speech response:', response)
    
    return response.content
