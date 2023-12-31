import random
import string
import sys

# Cmd to run: python3 1
# This will create 1 mb file.

file_size_mb = int(sys.argv[1])


def generate_random_content(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def create_file_with_content(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


file_size_bytes = file_size_mb * 1024 * 1024

random_content = generate_random_content(file_size_bytes)
file_name = 'file.txt'

create_file_with_content(file_name, random_content)

with open(file_name, 'r') as file:
    print(file.read())
