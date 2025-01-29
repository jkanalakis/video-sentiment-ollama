# transcription_alternative.py

import speech_recognition as sr
import ffmpeg
import streamlit as st
import os

def extract_audio_ffmpeg(video_path: str, audio_path: str) -> str:
    """
    Extracts audio from the given video file and saves it as a WAV file.

    Args:
        video_path (str): Path to the input video file.
        audio_path (str): Full path (including filename) where the extracted audio will be saved.

    Returns:
        str: Path to the extracted audio file.
    """
    try:
        st.write(f"Extracting audio from {video_path} to {audio_path}")
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, format='wav', acodec='pcm_s16le', ac=1, ar='16000')
            .run(overwrite_output=True)
        )
        return audio_path
    except ffmpeg.Error as e:
        if e.stderr:
            error_message = e.stderr.decode()
        else:
            error_message = "An unknown error occurred during audio extraction."
        st.error(f"FFmpeg error: {error_message}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

def transcribe_audio_speech_recognition(audio_path: str) -> str:
    """
    Transcribes the audio file to text using Google Speech Recognition via SpeechRecognition.

    Args:
        audio_path (str): Path to the audio file.

    Returns:
        str: Transcribed text.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand audio.")
        return ""
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    except Exception as e:
        st.error(f"An error occurred during transcription: {e}")
        return ""