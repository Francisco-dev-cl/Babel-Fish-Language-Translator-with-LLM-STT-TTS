# Babel Fish Language Translator (LLM, STT, & TTS)

This repository contains a full-stack, near-real-time voice translation application inspired by the fictional "Babel Fish," combining Speech-to-Text (STT), Large Language Models (LLMs) for contextual translation, and Text-to-Speech (TTS) synthesis.

## 🎯 Project Objective

The goal of this application is to engineer an end-to-end oral translation pipeline. It captures a user's spoken audio in a source language, transcribes it into text, uses an LLM to accurately translate the content while preserving cultural context, and converts the translated script into a natural audio broadcast.

## 📁 Repository Structure

* **`server.py`**: The central Flask application backend that exposes routing endpoints, serves client files, and handles network streams for media chunks.
* **`worker.py`**: The engine orchestration logic that acts as the pipeline manager, abstracting background API calls to transcription services, generative models, and voice synthesizers.
* **`templates/` & `static/`**: Front-end workspace housing HTML UI structures, CSS formatting styles, and critical JavaScript routines managing the browser microphone inputs via the Web Audio API.
* **`models/`**: System workspace containing template properties, targeted system prompts, or configuration dictionaries for specific translation profiles.
* **`Dockerfile` & `requirements.txt`**: Standardized blueprint stack compiling the machine learning configurations and server packages into an immutable, portable environment container.

## 🛠 Technologies Used

* **Server & Logic:** Python 3.x, Flask
* **Speech Processing:** Open-source or Cloud STT/TTS Engines (e.g., IBM Watson, Whisper, or cloud-based synthesis models)
* **Translation Core:** Large Language Models (LLM API wrappers)
* **DevOps Engineering:** Docker Containerization
* **Client Architecture:** HTML5, CSS3, JavaScript (Asynchronous fetch/media streams)

## 🚀 Installation and Execution

### Local Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Babel-Fish-Language-Translator-with-LLM-STT-TTS
   ```

2. **Install systemic ML packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Boot the localized Flask service:**
   ```bash
   python server.py
   ```

### Docker Platform Deployment

To isolate streaming and engine dependencies inside an isolated layer:

1. **Compile the image blueprint:**
   ```bash
   docker build -t babel-fish-translator .
   ```

2. **Initialize the live container path:**
   ```bash
   docker run -p 5000:5000 babel-fish-translator
   ```

## 📈 Demonstrated Skills

* **Comprehensive Speech Pipelines:** Successfully chaining individual audio capture, transcription, text manipulation, and audio synthesis stages into a single low-latency thread.
* **Contextual Language Translation:** Utilizing deep text generation prompts to handle multi-lingual conversions with better structural accuracy than traditional rigid word-to-word engines.
* **MLOps Package Standards:** Designing robust container steps to wrap multi-layered audio processing binaries (`ffmpeg`, audio drivers, etc.) seamlessly for production deployments.
