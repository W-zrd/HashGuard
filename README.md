## Description
HashGuard is a Python script that provides file integrity checking by generating hash values. HashGuard helps safeguard the integrity of your files, ensuring they remain unchanged and untampered with.

## Features

- Calculate hash values of files using different algorithms (e.g., MD5, SHA-256)
- **Single Mode**    : Checks the hash value of a file
- **Recursive Mode** : Checks the hash value of all files in the directory

## Requirements

- Python 3.x
- The required Python packages are listed in the `requirements.txt` file.
```
pip install -r requirements.txt
```



## How to use

You need to add flags or options when running HashGuard, i.e. single mode or recursive mode.

**Single Mode**

Specify the path to a single file with its format
```
python3 main.py -s tests/file.txt
```

**Recursive Mode**

Specify the path to a directory
```
python3 main.py -r tests
```

**Specifying Hash Algorithm**

By default, this program uses MD5 hash function. But, you can specify the hash algorithm by adding `-a` or `--algorithm` flags before /or after typing the scan mode.
```
python3 main.py -r tests -a sha512-224
```
or
```
python3 main.py -a sha3-512 -a tests/file.txt
```
Check the **Supported Hash Functions** section to see all of the hashes supported in this program

**Help Options**

If you are unsure about how to running it, you can type the following command.
```
python3 main.py --help
```
## Supported Hash Functions
 - MD5
 - SHA1
 - SHA224
 - SHA256
 - SHA384
 - SHA512
 - SHA512/224
 - SHA512/256
 - SHA3-224
 - SHA3-256
 - SHA3-384
 - SHA3-512

