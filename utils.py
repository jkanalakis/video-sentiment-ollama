import os
from typing import List
import shutil

def save_file(file, directory: str) -> str:
    """
    Saves the uploaded file to the specified directory.

    Args:
        file: The uploaded file object.
        directory (str): The directory where the file will be saved.

    Returns:
        str: Path to the saved file.
    """
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

def validate_file_extension(file, allowed_extensions: List[str]) -> bool:
    """
    Validates if the uploaded file has an allowed extension.

    Args:
        file: The uploaded file object.
        allowed_extensions (List[str]): List of allowed file extensions.

    Returns:
        bool: True if valid, False otherwise.
    """
    return any(file.name.lower().endswith(ext) for ext in allowed_extensions)

def clean_directory(directory: str):
    """
    Cleans the specified directory by deleting all files within it.

    Args:
        directory (str): The directory to clean.
    """
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory, exist_ok=True)