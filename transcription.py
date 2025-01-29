# transcription.py

# Remove or comment out the following function:

# from typing import List
# import ollama

# def transcribe_audio(audio_path: str) -> str:
#     """
#     Transcribes the audio file to text using a speech-to-text model via Ollama.

#     Args:
#         audio_path (str): Path to the audio file.

#     Returns:
#         str: Transcribed text.
#     """
#     response = ollama.chat(
#         model="wizardlm2",
#         messages=[
#             {
#                 'role': 'user',
#                 'content': 'Transcribe the following audio file accurately.',
#                 'audio': audio_path
#             }
#         ],
#         options={'temperature': 0}
#     )
#     return response['message']['content']