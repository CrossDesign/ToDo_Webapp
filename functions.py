""" Contains all functions for 'todo' project. """

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Returns lines in document as list variable."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """ Overwrites file content with first arg. """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello from 'Functions Module'")