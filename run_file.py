from file_class import *

file_1 = FileFunction('players.txt')
print(file_1.print_file())
print(file_1.read_file())
file_1.add_to_file('Origiii')
while True:
    user_file = input("Enter new file name:")
    if file_1.set_file_name(user_file):
        print("File changed")
        break
print(file_1.print_file())
