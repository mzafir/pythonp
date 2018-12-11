from sys import argv
from os import _exists

script, input_file=argv


def print_two(*args):
    test, test2 =args
    print(f"this is too bad {test} but not great either {test2}")



def print_line_count(line_count, f):
    print(line_count, f.readline())


def print_line_test(line, encoding, errors):
    next_lang=line.strip()
    raw_bytes=next_lang.encode(encoding,errors=errors)
    cooked_string=raw_bytes.decode(encoding, errors
current_file=open(input_file)

line_count=1

print_line_count(line_count, current_file)
line_count+=1
print(line_count,current_file)