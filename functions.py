def get_todos():
    """ Read a text file and return the list of to-do items.
    """
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath = "todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)