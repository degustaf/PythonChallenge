"""
Solution to mapping challenge at
http://www.pythonchallenge.com/pc/def/map.html
"""

def translate_data(data):
    """
    Performs ROT2 (rotation by 2) transformation on all lower case ASCII characters
    in data
    """
    start_num = int.from_bytes(b'a', byteorder='big')
    end_num = int.from_bytes(b'z', byteorder='big')

    def rot2(input_data):
        """
        Performs ROT2 (rotation by 2) transformation on a single lower case ASCII
        character in input_data.
        """
        if input_data < start_num:
            return input_data
        if input_data > end_num:
            return input_data
        result = input_data + 2
        if result > end_num:
            result += start_num - end_num - 1
        return result

    data_b = data.encode()
    data_b = bytearray([rot2(x) for x in data_b])
    data = data_b.decode()
    print(data)

if __name__ == "__main__":
    with open('data/data_01.txt', 'r') as f:
        translate_data(f.read())

    translate_data("map")
