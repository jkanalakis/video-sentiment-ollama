# utils.py

import os
from typing import List
import shutil
import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_file(file, directory: str) -> str:
    """
    Saves the uploaded file to the specified directory.

    Args:
        file: The uploaded file object.
        directory (str): The directory where the file will be saved.

    Returns:
        str: Path to the saved file.
    """
    try:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        logger.info(f"File saved to {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"Error saving file: {e}")
        st.error(f"Error saving file: {e}")
        return None

def validate_file_extension(file, allowed_extensions: List[str]) -> bool:
    """
    Validates if the uploaded file has an allowed extension.

    Args:
        file: The uploaded file object.
        allowed_extensions (List[str]): List of allowed file extensions.

    Returns:
        bool: True if valid, False otherwise.
    """
    is_valid = any(file.name.lower().endswith(ext) for ext in allowed_extensions)
    if not is_valid:
        logger.warning(f"Invalid file extension for file: {file.name}")
    return is_valid

def clean_directory(directory: str):
    """
    Cleans the specified directory by deleting all files within it.

    Args:
        directory (str): The directory to clean.
    """
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory, exist_ok=True)
        logger.info(f"Directory cleaned: {directory}")
    except Exception as e:
        logger.error(f"Error cleaning directory {directory}: {e}")
        st.error(f"Error cleaning directory {directory}: {e}")