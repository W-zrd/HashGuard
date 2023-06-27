import hashlib
import os

def singleMode(path, crypto="md5"):
    obj = hashlib.new(crypto)
    with open(path, 'rb') as file:
        for i in iter(lambda: file.read(4096), b''):
            obj.update(i)
    return obj.hexdigest()

def recursiveMode(directory_path, crypto="md5"):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = singleMode(file_path, crypto)
            print(f"File: {file_path}")
            print(f"Hash ({crypto.upper()}): {hash_value}\n")

# Recursive Mode
Rpath = "tests"
hashed = recursiveMode(Rpath, crypto="sha256")

# Single Mode
Spath = "tests/file.txt"
hashed = singleMode(Spath, crypto="sha256")

print(f"Hash value: {hashed}")
