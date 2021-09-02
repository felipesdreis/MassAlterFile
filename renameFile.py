import os 
import sys

counter = 0
path = os.getcwd() + "\\<path>"
print('path to use', path)
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, file.replace("<old>", "<new>")))
    print(file)
