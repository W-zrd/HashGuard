import hashlib
import os

def singleMode(path, algorithm="md5"):
    obj = hashlib.new(algorithm)
    with open(path, 'rb') as file:
        for i in iter(lambda: file.read(4096), b''):
            obj.update(i)
    return obj.hexdigest()

def recursiveMode(directory_path, algorithm="md5"):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = singleMode(file_path, algorithm)
            print(f"File: {file_path}")
            print(f"Hash ({algorithm.upper()}): {hash_value}\n")

