FILEPATH = 'todos.txt'

def read_file(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:     # read an external file with exception handling
        todos_local = file_local.readlines()
    return todos_local


def write_file(todos_arg, filepath=FILEPATH):
    # writing to text file with exception handling
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # writelines() overwrites existing contents in text file

