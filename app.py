import streamlit as st
from audio_extraction import extract_audio, validate_video_file
from transcription import transcribe_audio, split_transcript
from sentiment_analysis import analyze_sentiment, aggregate_sentiments
from visualization import plot_sentiment_trends, display_summary_statistics
from utils import save_file, validate_file_extension

def main():
    st.title("Video Sentiment Analysis Dashboard")
    st.markdown("""
        Upload a video to analyze its sentiment. The app will extract the audio, transcribe it, perform sentiment analysis, and display the results.
    """)
    
    # Step 1: Video Upload
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov", "mkv"])
    
    if uploaded_file:
        if not validate_file_extension(uploaded_file, ["mp4", "avi", "mov", "mkv"]):
            st.error("Unsupported file type.")
            return
        
        # Save the uploaded video
        video_path = save_file(uploaded_file, "uploaded_videos/")
        
        # Step 2: Audio Extraction
        audio_path = extract_audio(video_path, "extracted_audio/")
        st.success("Audio extracted successfully.")
        
        # Step 3: Transcription
        transcript = transcribe_audio(audio_path)
        st.text_area("Transcribed Text", transcript, height=300)
        
        # Step 4: Sentiment Analysis
        sentiment_results = [analyze_sentiment(chunk) for chunk in split_transcript(transcript)]
        aggregated_sentiment = aggregate_sentiments(sentiment_results)
        
        # Step 5: Visualization
        plot_sentiment_trends(aggregated_sentiment)
        display_summary_statistics(aggregated_sentiment)

if __name__ == "__main__":
    main()