import hashlib

def hash(path, crypto="md5"):
    obj = hashlib.new(crypto)
    with open(path, 'rb') as file:
        for i in iter(lambda: file.read(4096), b''):
            obj.update(i)
    return obj.hexdigest()

# Usage example
path = "/path/to/your/file.format"
hashed = hash(path, crypto="sha256")
print(f"Hash value: {hashed}")
