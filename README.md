# AI Personal Assistant Project

# Overview

This project is an AI-powered personal assistant built using Streamlit, Hugging Face Transformers, and TensorFlow. It provides two main functionalities:

Text-based query handling with AI-generated responses.

Voice query handling by transcribing audio inputs and generating AI responses.

The app is lightweight, user-friendly, and designed to run efficiently even on resource-constrained devices by utilizing smaller models like gpt2 for text generation and openai/whisper-tiny for speech recognition.

# Features

1. Text Query Handling

Accepts user inputs as text prompts.

Generates coherent and relevant responses using the GPT-2 model for text generation.

Limits response length to prevent overloading resources.

2. Voice Query Handling

Accepts audio file uploads in .wav or .mp3 formats.

Transcribes the audio into text using OpenAI Whisper-Tiny.

Processes the transcribed text to generate an AI response.

3. System Monitoring

Displays available and total memory using the psutil library in the app's sidebar.

4. Device Information

Displays whether TensorFlow is using a GPU or CPU for computations.

# Technologies Used

1. Streamlit

Framework for building the user interface.

Provides interactive components like text input, file uploaders, and spinners for a smooth user experience.

2. Hugging Face Transformers

Text Generation: GPT-2 is used for generating text-based responses.

Speech Recognition: Whisper-Tiny is employed for transcribing audio inputs into text.

3. TensorFlow

Used to check the hardware being utilized (GPU or CPU).

4. Psutil

Monitors system memory to ensure the app's resource efficiency.

# Installation and Setup

Prerequisites

Python 3.8 or higher.

Virtual environment (optional but recommended).

Dependencies installed from requirements.txt.

Steps

Clone the Repository:

git clone <repository_url>
cd <repository_name>

Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Run the Application:

streamlit run app.py

Access the App:

Open your browser and navigate to http://localhost:8501.

Directory Structure

project-folder/
├── app.py               # Main Streamlit application
├── requirements.txt     # List of Python dependencies
├── README.md           # Detailed project documentation

# Key Functionalities and Code Breakdown

1. Memory Monitoring

Function: check_memory()

Description: Uses psutil to display available and total memory in MB within the app's sidebar.

2. Model Loading

Function: load_models()

Description: Caches the Hugging Face pipelines for text generation and speech recognition to avoid redundant loading and improve performance.

Models Used:

gpt2 for text generation.

openai/whisper-tiny for speech recognition.

3. Text Query Handling

Function: handle_text_query(query)

Description: Generates text responses for user input using the text generation pipeline.

4. Voice Query Handling

Function: handle_voice_query(audio_path)

Description: Transcribes audio input into text and processes the transcription to generate a response.

5. Device Information

TensorFlow Check:

Displays whether TensorFlow is utilizing GPU(s) or CPU.

Uses tf.config.list_physical_devices('GPU').

# Example Usage

Text Query

Enter a prompt in the Text Query section.

Click "Enter" and wait for the response.

The AI response will be displayed below the input field.

Voice Query

Upload an audio file in .wav or .mp3 format in the Voice Query section.

Wait for the transcription and AI-generated response to appear.

# Dependencies

Streamlit: pip install streamlit

Hugging Face Transformers: pip install transformers

Psutil: pip install psutil

TensorFlow: pip install tensorflow

Error Handling

Model Loading Errors:

Displays an error message if models fail to load.

Ensures the app does not crash unexpectedly.

Invalid File Uploads:

Handles unsupported file formats and provides appropriate feedback to the user.

# Low System Resources:

Memory monitoring provides real-time insights to prevent resource overloads.

# Limitations

The app uses smaller models (GPT-2 and Whisper-Tiny) to optimize for resource usage. For higher performance, larger models can be integrated but may require more computational power.

Only supports .wav and .mp3 audio file formats.

# Future Enhancements

Multi-language Support:

Extend the app to handle queries in multiple languages.

Larger Models:

Provide an option for users with high-end systems to switch to larger, more advanced models for better accuracy.

Real-time Speech Recognition:

Implement real-time transcription for live audio inputs.

Conversation History:

Save and display past interactions to enhance user experience.

# Acknowledgments

Streamlit: For the interactive web app framework.

Hugging Face: For providing state-of-the-art pre-trained models.

TensorFlow: For GPU/CPU resource monitoring.

Psutil: For system monitoring capabilities.

# License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.

# Contact

For queries or contributions, please contact:

Name: Muhammad Anas Akhtar

Email: muhammadanasakhtar19@gmail.com
