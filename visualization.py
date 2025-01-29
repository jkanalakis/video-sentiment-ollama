# visualization.py

import streamlit as st
import matplotlib.pyplot as plt

def plot_sentiment_trends(sentiment_data: dict):
    """
    Plots sentiment trends using Streamlit charts.

    Args:
        sentiment_data (dict): Dictionary containing sentiment counts.
    """
    sentiments = list(sentiment_data.keys())
    counts = list(sentiment_data.values())
    
    fig, ax = plt.subplots()
    ax.bar(sentiments, counts, color=['green', 'red', 'grey'])
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_title('Sentiment Distribution')
    
    st.pyplot(fig)

def display_summary_statistics(sentiment_data: dict):
    """
    Displays summary statistics of sentiment analysis.

    Args:
        sentiment_data (dict): Dictionary containing sentiment counts.
    """
    total = sum(sentiment_data.values())
    if total == 0:
        st.write("No sentiment data available.")
        return
    
    st.write(f"**Total Analyzed Segments:** {total}")
    for sentiment, count in sentiment_data.items():
        percentage = (count / total) * 100
        st.write(f"**{sentiment}:** {count} ({percentage:.2f}%)")