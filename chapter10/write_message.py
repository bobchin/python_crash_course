from os import path, remove

filename = path.join(path.dirname(__file__), "programming.txt")
if path.exists(filename):
    remove(filename)

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also oove finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

