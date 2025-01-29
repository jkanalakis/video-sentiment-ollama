# app.py

import streamlit as st
import os

from transcription_alternative import extract_audio_ffmpeg, transcribe_audio_speech_recognition
from sentiment_analysis import analyze_sentiment, aggregate_sentiments, split_transcript
from visualization import plot_sentiment_trends, display_summary_statistics
from utils import save_file, validate_file_extension

def main():
    st.title("Video Sentiment Analysis")
    st.markdown("""
        Upload a video to analyze its sentiment. The app will extract the audio, transcribe it, perform sentiment analysis, and display the results.
    """)

    # Initialize session state variables
    if 'video_path' not in st.session_state:
        st.session_state.video_path = None
    if 'audio_path' not in st.session_state:
        st.session_state.audio_path = None
    if 'transcript' not in st.session_state:
        st.session_state.transcript = None

    # Step 1: Video Upload
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file and st.session_state.video_path is None:
        if not validate_file_extension(uploaded_file, ["mp4", "avi", "mov", "mkv"]):
            st.error("Unsupported file type.")
        else:
            # Save the uploaded video
            video_path = save_file(uploaded_file, "videos/")
            if video_path:
                st.session_state.video_path = video_path
                st.success(f"Video uploaded successfully: {uploaded_file.name}")
            else:
                st.error("Failed to save the uploaded video.")

    # Step 2: Audio Extraction
    if st.session_state.video_path:
        if st.button("Extract Audio") and st.session_state.audio_path is None:
            # Define the audio filename based on the video filename
            audio_filename = os.path.splitext(os.path.basename(st.session_state.video_path))[0] + ".wav"  # Using WAV for SpeechRecognition
            audio_path = os.path.join("audio", audio_filename)

            # Debugging: Display the audio path
            st.write(f"Extracting audio to: {audio_path}")

            # Extract audio using the correct file path
            extracted_audio_path = extract_audio_ffmpeg(st.session_state.video_path, audio_path)

            if extracted_audio_path:
                st.session_state.audio_path = extracted_audio_path
                st.success("Audio extracted successfully.")
                st.audio(extracted_audio_path)
            else:
                st.error("Audio extraction failed.")

    # Step 3: Transcription
    if st.session_state.audio_path:
        if st.button("Transcribe Audio") and st.session_state.transcript is None:
            with st.spinner("Transcribing audio..."):
                transcript = transcribe_audio_speech_recognition(st.session_state.audio_path)
                if transcript:
                    st.session_state.transcript = transcript
                    st.success("Transcription completed!")
                    st.text_area("Transcribed Text", transcript, height=300)

                    # Step 4: Sentiment Analysis
                    sentiment_results = [analyze_sentiment(chunk) for chunk in split_transcript(transcript)]
                    aggregated_sentiment = aggregate_sentiments(sentiment_results)

                    # Step 5: Visualization
                    plot_sentiment_trends(aggregated_sentiment)
                    display_summary_statistics(aggregated_sentiment)
                else:
                    st.error("Transcription failed.")

    # Optional: Reset Button to Clear Session State
    if st.button("Reset"):
        for key in ['video_path', 'audio_path', 'transcript']:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()

if __name__ == "__main__":
    main()