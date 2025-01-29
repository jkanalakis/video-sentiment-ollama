# Video Sentiment Analysis Dashboard

A web-based application built with [Streamlit](https://streamlit.io/), [LangChain](https://github.com/hwchase17/langchain), [Ollama](https://ollama.ai/), and [moviepy](https://github.com/Zulko/moviepy). This dashboard allows users to upload video files, extract and transcribe audio, perform sentiment analysis on the transcribed text, and visualize sentiment trends over time.

## Features

- **Video Uploading:**  
  Simple interface to upload video files in formats like `.mp4`, `.avi`, `.mov`, and `.mkv`.

- **Audio Extraction:**  
  Utilizes `moviepy` to extract audio from uploaded videos.

- **Transcription:**  
  Converts extracted audio to text using a speech-to-text model (`wizardlm2`) via Ollama.

- **Sentiment Analysis:**  
  Analyzes the sentiment of the transcribed text using an LLM (`Llama 3.2 3b`).

- **Visualization:**  
  Displays sentiment trends and summary statistics using interactive Streamlit charts.

- **Modular Design:**  
  Organized into separate modules for audio extraction, transcription, sentiment analysis, and visualization for better maintainability and scalability.

## Getting Started

### Prerequisites

1. **Python 3.8+**  
   Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).

2. **Ollama**  
   This app relies on Ollama’s language models. Refer to [Ollama’s documentation](https://ollama.ai/docs) for installation and configuration instructions.

3. **Model Downloads**  
   - **Transcription Model (`wizardlm2`):**  
     ```bash
     ollama pull wizardlm2
     ```
   - **Sentiment Analysis Model (`Llama 3.2 3b`):**  
     ```bash
     ollama pull llama3.2-3b
     ```

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/video-sentiment-analysis-dashboard.git