import os
import platform


def open_file(file_path: str):
    """
    Open a file using the default application for the file type.

    Parameters:
    file_path (str): The path to the file to open.

    Returns:
    None
    """
    if platform.system() == "Darwin":  # macOS
        os.system(f"open {file_path}")
    elif platform.system() == "Windows":  # Windows
        os.system(f"start {file_path}")
    else:  # Linux
        os.system(f"xdg-open {file_path}")
