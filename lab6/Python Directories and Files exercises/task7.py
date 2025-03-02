def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())


copy_file("source.txt", "destination.txt")  # Replace with actual file names
