#№1
import os

path = 'C:\\Users\\жания\\Desktop\\PP2\\Labs'
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("1)", directories)
print(files)
#№2
access_info = {
    'exists': os.path.exists(path),
    'readable': os.access(path, os.R_OK),
    'writable': os.access(path, os.W_OK),
    'executable': os.access(path, os.X_OK)
}
print("2) Access Info:", access_info)
#№3
print("№3")
if os.path.exists(path):
    file = os.path.basename(path)
    directory = os.path.dirname(path)
    print(file)
    print(directory)
else:
    print("Path does not exist")
#№4
file = 'C:\\Users\\жания\\Desktop\\PP2\\Labs\\lab 6\\task.txt'
with open(file, 'r') as file:
    cnt = sum(1 for line in file)
print("4)", cnt)