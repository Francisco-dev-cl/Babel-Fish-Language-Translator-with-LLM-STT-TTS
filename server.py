from flask import Flask, render_template, request, json
from flask_cors import CORS
from worker import speech_to_text, text_to_speech, watsonx_process_message
import os
import base64

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    """Renders the main frontend interface."""
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    """Endpoint to transcribe user audio input."""
    print("processing Speech-to-Text")
    audio_binary = request.data # Get audio binary from the request body
    
    text = speech_to_text(audio_binary)
    
    # Return the transcribed text as a JSON response
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/process-message', methods=['POST'])
def process_message_route():
    """Endpoint to process translation and convert the result to speech."""
    user_message = request.json['userMessage']
    voice = request.json['voice']
    print(f'User message: {user_message}, Preferred voice: {voice}')

    # 1. Get translation from Watsonx
    watsonx_response_text = watsonx_process_message(user_message)
    
    # 2. Clean response (remove empty lines)
    watsonx_response_text = os.linesep.join([s for s in watsonx_response_text.splitlines() if s])
    
    # 3. Convert translated text to speech audio
    watsonx_response_speech = text_to_speech(watsonx_response_text, voice)
    
    # 4. Encode audio to base64 string for JSON transmission
    watsonx_response_speech = base64.b64encode(watsonx_response_speech).decode('utf-8')

    # Return both text and speech data to the frontend
    response = app.response_class(
        response=json.dumps({
            "watsonxResponseText": watsonx_response_text, 
            "watsonxResponseSpeech": watsonx_response_speech
        }),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
