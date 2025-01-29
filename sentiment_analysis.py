def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of the provided text using an LLM.

    Args:
        text (str): Text to analyze.

    Returns:
        str: Sentiment classification (e.g., Positive, Negative, Neutral).
    """
    response = ollama.chat(
        model="llama3.2-3b",
        messages=[
            {
                'role': 'user',
                'content': f"Analyze the sentiment of the following text: \"{text}\". Respond with Positive, Negative, or Neutral."
            }
        ],
        options={'temperature': 0}
    )
    return response['message']['content'].strip()

def aggregate_sentiments(sentiment_results: List[str]) -> dict:
    """
    Aggregates sentiment analysis results.

    Args:
        sentiment_results (List[str]): List of sentiment classifications.

    Returns:
        dict: Dictionary with sentiment counts.
    """
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for sentiment in sentiment_results:
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1
    return sentiment_counts