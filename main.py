import argparse
import scan_modes

parser = argparse.ArgumentParser(description="Hash Integrity Checker")

parser.add_argument("-s", "--single", 
                    help="Path to a single file (Single Mode). ex: python3 main.py -s /path/to/file.format")

parser.add_argument("-r", "--recursive",
                     help="Path to a directory (Recursive Mode). ex: python3 main.py -r /path/to/directory")

parser.add_argument("-a", "--algorithm", default="md5", 
                    help="Hash algorithm, ex: sha1, sha256, md5. (default: md5)")

args = parser.parse_args()

# Single Mode Scan
if args.single:
    Fpath = args.single
    hash_value = scan_modes.singleMode(Fpath, algorithm=args.algorithm)
    print(f"File: {Fpath}")
    print(f"Hash ({args.algorithm.upper()}): {hash_value}")

# Recursive Mode Scan
elif args.recursive:
    Dpath = args.recursive
    scan_modes.recursiveMode(Dpath, algorithm=args.algorithm)

else:
    print("Please provide either a single mode scan (-s) or a recursive mode scan (-r)")
