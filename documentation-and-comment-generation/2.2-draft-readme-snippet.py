#!/usr/bin/env python3
import argparse
import sys
from utils import read_json_file, write_json_file

def count_lines(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

def to_uppercase(path: str):
    for line in open(path, 'r', encoding='utf-8'):
        print(line.strip().upper())

def convert_json(input_path: str, output_path: str):
    data = read_json_file(input_path)
    write_json_file(data, output_path)

def main():
    parser = argparse.ArgumentParser(prog='cli_tool')
    sub = parser.add_subparsers(dest='command')

    p1 = sub.add_parser('count', help='Count lines in a file')
    p1.add_argument('file', help='Path to text file')

    p2 = sub.add_parser('upper', help='Print file in uppercase')
    p2.add_argument('file', help='Path to text file')

    p3 = sub.add_parser('json-convert', help='Convert JSON file')
    p3.add_argument('input', help='Input JSON file')
    p3.add_argument('output', help='Output JSON file')

    args = parser.parse_args()

    if args.command == 'count':
        print(count_lines(args.file))
    elif args.command == 'upper':
        to_uppercase(args.file)
    elif args.command == 'json-convert':
        convert_json(args.input, args.output)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()