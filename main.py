import argparse
import scan_modes

parser = argparse.ArgumentParser(description="Hash Integrity Checker")

parser.add_argument("-s", "--single")
parser.add_argument("-r", "--recursive")
parser.add_argument("-a", "--algorithm", default="sha1", help="Hash algorithm (default: sha1)")

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
