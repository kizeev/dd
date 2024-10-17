import re

from ast import literal_eval


def deobfuscate(encoded_string):
    base64_alphabet = (
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/')

    result = ''
    temp = 0
    bit_count = 0

    for char in encoded_string:
        if char == '=':
            break
        char_index = base64_alphabet.index(char)
        temp |= char_index << (18 - bit_count * 6)
        bit_count += 1
        if bit_count == 4:
            result += chr((temp >> 16) & 0xFF)
            result += chr((temp >> 8) & 0xFF)
            result += chr(temp & 0xFF)
            temp = 0
            bit_count = 0

    if bit_count:
        if bit_count == 3:
            result += chr((temp >> 16) & 0xFF)
            result += chr((temp >> 8) & 0xFF)
        elif bit_count == 2:
            result += chr((temp >> 16) & 0xFF)

    return result


def find_encoded_array_in_js_file(text):
    pattern = r'function \w\(\) \{\s+var \w = (\[[^\]]+\]);'
    encoded_array = re.findall(pattern, text)[0]
    return literal_eval(encoded_array)


def find_array_shift(text):
    pattern = r'\b\w\[\w -= (\d+)\]'
    shift = re.findall(pattern, text)[0]
    return int(shift)


def get_decoded_item(encoded_chunk, decoded_array, array_shift):
    chunk_index = int(re.findall(r'\d+', encoded_chunk)[0])
    res = f"'{decoded_array[chunk_index - array_shift]}'"
    # print(f'{encoded_chunk}>>>{res}')
    return res


def unescape_hex_string(escaped_string):
    def hex_to_char(match):
        return chr(int(match.group(0)[1:], 16))
    escaped_string = escaped_string.replace('\\', '')
    return re.sub(r'x[0-9a-fA-F]{2}', hex_to_char, escaped_string)


def main(js_file_path):
    with open(js_file_path) as f:
        escaped_js_text = f.read()

    js_text = unescape_hex_string(escaped_js_text)
    encoded_array = find_encoded_array_in_js_file(js_text)
    decoded_array = [deobfuscate(i) for i in encoded_array]
    print('>>>array:', decoded_array)
    array_shift = find_array_shift(js_text)
    print('\n>>>shift:', array_shift)

    encoded_chunk_pattern = r'\b\w\(\d{3}\)'
    decoded_js_text = re.sub(
        encoded_chunk_pattern,
        lambda x: get_decoded_item(x.group(), decoded_array, array_shift),
        js_text)

    with open('versions/actual_tags_decoded.js', 'w') as f:
        f.write(decoded_js_text)


if __name__ == '__main__':
    js_file = 'versions/actual_tags.js'
    main(js_file)
