# utils/file_detector.py
# ─────────────────────────────────────────────────────────────
# Utility to detect file type from file extension.
# Called by the ingestion agent before loading any document.
# ─────────────────────────────────────────────────────────────

from pathlib import Path
from config import SUPPORTED_EXTENSIONS

def detect_file_type(file_path : str) -> str:
    """
    Takes a file path string and returns the file type 

    Args:
        file_path (str) : full or relative path to the file   

    Returns:
        one of : "pdf", "excel", "csv", "word", "text","unsupported"
    """
    
    # Path() turns a string like "folder/file.pdf"
    # into a proper path object we can work with

    path = Path(file_path)

    # .suffix gives us the extension e.g. ".pdf", ".xlsx"
    # .lower() handles cases like ".PDF" or ".XLSX"
    extension = path.suffix.lower()

    # Check if the file even exists on disk
    if not path.exists():
        raise FileNotFoundError(f"File not found:{file_path}")  
    
    if extension not in SUPPORTED_EXTENSIONS:
        return "unsupported"
    
    if extension == ".pdf":
        return "pdf"
    
    elif extension in [".xlsx",".xls"]:
        return "excel"
    
    elif extension == ".csv":
        return "csv"
    
    elif extension == ".docx":
        return "word"
    
    elif extension == ".txt":
        return "text"
    
    else:
        return "unsupported"
    
def get_file_info(file_path : str) -> dict:
    """
    Returns basic metadata about the file.
    This gets stored in state["file_metadata"].

    Args :
        file_path : full or relative path to the file 

    Returns:
        dict with file name , type , size in KB 
    """
    path = Path(file_path)
    file_type = detect_file_type(file_path)

    return {
        "file_name" : path.name,
        "file_type" : file_type,
        "file_size_kb" : round(path.stat().st_size / 1024, 2),
        "file_path" : str(path.resolve()) 
    }







