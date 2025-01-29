# audio_extraction.py

import os
from moviepy.editor import VideoFileClip
import streamlit as st  # Ensure Streamlit is imported if used for error handling

def extract_audio(video_path: str, output_audio_path: str) -> str:
    """
    Extracts audio from the given video file and saves it as a WAV file.

    Args:
        video_path (str): Path to the input video file.
        output_audio_path (str): Full path (including filename) where the extracted audio will be saved.

    Returns:
        str: Path to the extracted audio file.
    """
    os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_audio_path, codec='pcm_s16le')  # WAV format
        video_clip.close()
        audio_clip.close()
        return output_audio_path
    except Exception as e:
        st.error(f"Error extracting audio: {e}")
        return None