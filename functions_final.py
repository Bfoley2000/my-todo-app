# Example of a module
# Function examples are below

FILEPATH = "todos_final.txt"


def get_todos(filepath=FILEPATH):   # Example of default argument
    # Example of doc string
    """
    Reads a text file and
    returns the list of to-do items
    """

    # Example of 'with' context manager
    with open(filepath, 'r') as file_local:
        items = file_local.readlines()
    return items

# Example of outputting a doc string
# print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write a to-do item list in the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# This only executes if functions.py is run
# __name__ is "__main__" when you run functions.py
# Otherwise, __name__ is "functions"
# This script is only executed when the main file (this file) is executed
if __name__ == "__main__":
    print("Executing functions.py")