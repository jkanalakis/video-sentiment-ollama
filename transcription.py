from typing import List
import ollama

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribes the audio file to text using a speech-to-text model via Ollama.

    Args:
        audio_path (str): Path to the audio file.

    Returns:
        str: Transcribed text.
    """
    response = ollama.chat(
        model="wizardlm2",
        messages=[
            {
                'role': 'user',
                'content': 'Transcribe the following audio file accurately.',
                'audio': audio_path
            }
        ],
        options={'temperature': 0}
    )
    return response['message']['content']

def split_transcript(transcript: str, max_length: int = 1000) -> List[str]:
    """
    Splits the transcript into chunks to facilitate sentiment analysis.

    Args:
        transcript (str): The full transcribed text.
        max_length (int, optional): Maximum length of each chunk. Defaults to 1000.

    Returns:
        List[str]: List of text chunks.
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