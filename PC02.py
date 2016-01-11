"""
Solution to mapping challenge at
http://www.pythonchallenge.com/pc/def/ocr.html
"""
from collections import defaultdict
from re import findall

def count_chars(data):
    """
    Count the occurence of Characters in data.
    """
    counts = defaultdict(int)
    for char in list(data):
        counts[char] += 1
    for char in sorted(counts, key=counts.get):
        print("{}\t{}".format(char, counts[char]))

def find_chars(data):
    """
    Find just the alphabetic characters in data.
    """
    result = "".join(findall("[a-zA-Z]+", data))
    print(result)

def main():
    """
    Main program for if this module is called as a standalone program.
    """
    with open('data/data_02.txt', 'r') as data_file:
        source = data_file.read()
        count_chars(source)
        find_chars(source)

if __name__ == "__main__":
    main()
