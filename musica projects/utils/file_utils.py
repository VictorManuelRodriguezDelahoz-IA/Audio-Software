import os

def save_temp_file(upload_file, temp_dir="temp"):
    """
    Guarda un archivo temporalmente en el sistema.
    """
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, upload_file.filename)
    with open(file_path, "wb") as f:
        f.write(upload_file.file.read())
    return file_path
