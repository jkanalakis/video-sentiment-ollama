import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path: str, output_audio_dir: str) -> str:
    """
    Extracts audio from the given video file and saves it as an MP3.

    Args:
        video_path (str): Path to the input video file.
        output_audio_dir (str): Directory where the extracted audio will be saved.

    Returns:
        str: Path to the extracted audio file.
    """
    os.makedirs(output_audio_dir, exist_ok=True)
    audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"
    audio_path = os.path.join(output_audio_dir, audio_filename)
    
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    
    video_clip.close()
    audio_clip.close()
    
    return audio_path

def validate_video_file(file) -> bool:
    """
    Validates the uploaded video file.

    Args:
        file: The uploaded file object.

    Returns:
        bool: True if valid, False otherwise.
    """
    allowed_extensions = ["mp4", "avi", "mov", "mkv"]
    return any(file.name.lower().endswith(ext) for ext in allowed_extensions)