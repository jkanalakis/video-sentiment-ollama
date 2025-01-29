# sentiment_analysis.py

from typing import List
from textblob import TextBlob
import streamlit as st

def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of the given text and returns 'Positive', 'Negative', or 'Neutral'.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def aggregate_sentiments(sentiment_results: List[str]) -> dict:
    """
    Aggregates sentiment results into a dictionary with counts for each sentiment category.
    """
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for sentiment in sentiment_results:
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1
    return sentiment_counts

def split_transcript(transcript: str, max_length: int = 1000) -> List[str]:
    """
    Splits the transcript into chunks to facilitate sentiment analysis.

    Args:
        transcript (str): The full transcribed text.
        max_length (int): Maximum number of characters per chunk.

    Returns:
        List[str]: A list of text chunks.
    """
    words = transcript.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1  # +1 for space
        if current_length >= max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks