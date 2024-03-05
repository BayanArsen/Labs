#Exercise 5
list = ["PP2", "Calculus", "Physics"]

with open('C:\\Users\\жания\\Desktop\\PP2\\Labs\\lab 6\\task.txt', "w") as file:
    for item in list:
        file.write(item + "\n")
##### Exercise 7
with open('C:\\Users\\жания\\Desktop\\PP2\\Labs\\lab 6\\task.txt', "r") as source_file:
    with open('C:\\Users\\жания\\Desktop\\PP2\\Labs\\lab 6\\deleting.txt', "w") as dest_file:
        dest_file.write(source_file.read())