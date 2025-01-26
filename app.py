import streamlit as st
from transformers import pipeline
import psutil
import tensorflow as tf

# Set the page configuration at the very beginning
st.set_page_config(page_title="AI Personal Assistant", page_icon="🤖", layout="centered")

# Sidebar: Memory Monitor
st.sidebar.header("System Info")

def check_memory():
    """Check and display system memory."""
    memory = psutil.virtual_memory()
    st.sidebar.write(f"**Available Memory:** {memory.available // (1024**2)} MB")
    st.sidebar.write(f"**Total Memory:** {memory.total // (1024**2)} MB")

check_memory()

# Caching models for optimization
@st.cache_resource
def load_models():
    """Load text generation and speech recognition pipelines."""
    try:
        text_gen_pipeline = pipeline(
            "text-generation",
            model="gpt2",  # Smaller model for text generation
            torch_dtype="auto"
        )
        speech_rec_pipeline = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny",  # Smaller model for speech recognition
            torch_dtype="auto"
        )
        return text_gen_pipeline, speech_rec_pipeline
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

# Load models
with st.spinner("Loading AI models..."):
    text_gen_pipeline, speech_rec_pipeline = load_models()

if not text_gen_pipeline or not speech_rec_pipeline:
    st.error("Failed to load one or more models. Please check your setup.")

# Functions
def handle_text_query(query):
    """Generate text response for a user query."""
    try:
        response = text_gen_pipeline(query, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error generating text: {e}"

def handle_voice_query(audio_path):
    """Process voice input and return transcription and AI-generated response."""
    try:
        transcription = speech_rec_pipeline(audio_path)['text']
        response = handle_text_query(transcription)
        return transcription, response
    except Exception as e:
        return None, f"Error processing voice query: {e}"

# Streamlit App Layout
st.title("AI Personal Assistant")
st.write("Welcome to your AI-powered personal assistant! Use this app to leverage the power of AI for various tasks.")

# Text Query Section
st.subheader("Text Query")
user_input = st.text_input("Enter a prompt:")

if user_input:
    with st.spinner("Processing your query..."):
        response = handle_text_query(user_input)
        if "Error" not in response:
            st.success("Response generated successfully!")
            st.write("**AI Response:**", response)
        else:
            st.error(response)

# Voice Query Section
st.subheader("Voice Query")
uploaded_audio = st.file_uploader("Upload an audio file (e.g., .wav, .mp3):", type=["wav", "mp3"])

if uploaded_audio:
    with st.spinner("Processing audio..."):
        transcription, response = handle_voice_query(uploaded_audio)
        if transcription:
            st.success("Audio processed successfully!")
            st.write("**Transcription:**", transcription)
            st.write("**AI Response:**", response)
        else:
            st.error(response)

# Device Information Section
st.subheader("Device Information")
gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
    st.write("**TensorFlow is using GPU:**")
    for device in gpu_devices:
        st.write(device.name)
else:
    st.write("**TensorFlow is using CPU.**")

# Footer
st.write("---")
st.write("App built using [Streamlit](https://streamlit.io/) and [Hugging Face Transformers](https://huggingface.co/transformers/).")
