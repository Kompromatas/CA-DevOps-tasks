def file_read(file_path):
    """
    Reads the content of a file and returns it as a list of lines.
    
    :param file_path: Path to the file to be read.
    :return: List of lines in the file.
    """
    with open(file_path, "r") as file:
        return file.readlines()


lines = file_read(input("Enter the path to the file: "))


print(f"Number of lines in Readme.md: {len(lines)}")