import os

file = "C:\\Users\\жания\\Desktop\\PP2\\Labs\\lab 6\\deleting.txt"

if os.path.exists(file):
    if os.access(file, os.W_OK):
        os.remove(file)
        print("File deleted")
    else:
        print("No write access to the file.")
else:
    print("None.")