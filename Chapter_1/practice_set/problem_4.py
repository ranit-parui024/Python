import os

def print_directory_contents(path='/'):
    """
    Print names of all files and directories in the given path.
    If no path is given, prints contents of current working directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
        return

    for name in entries:
        print(name)

if __name__ == "__main__":
    # Example: print contents of current directory
    print_directory_contents()

    # Example: print contents of a specified directory
    # print_directory_contents("/path/to/some/directory")
