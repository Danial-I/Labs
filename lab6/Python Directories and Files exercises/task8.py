import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"File {path} deleted.")
    else:
        print("File does not exist or cannot be deleted.")

# Example usage
delete_file("example.txt")  # Replace with actual file name


