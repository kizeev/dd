import json
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
    pattern = r'function a\(\) \{\s+var \w = (\[[^\]]+\]);'
    encoded_array = re.findall(pattern, text)[0]
    return literal_eval(encoded_array)


def find_array_shift(text):
    pattern = r'\b\w\[\w -= (\d+)\]'
    shift = re.findall(pattern, text)[0]
    return int(shift)


def get_decoded_item(encoded_chunk, decoded_array, array_shift):
    chunk_index = int(re.findall(r'\d+', encoded_chunk)[0])
    return decoded_array[chunk_index - array_shift]


def main(js_file_path):
    with open(js_file_path) as f:
        js_text = f.read()

    encoded_array = find_encoded_array_in_js_file(js_text)
    decoded_array = [deobfuscate(i) for i in encoded_array]
    print('>>>array:', decoded_array)
    array_shift = find_array_shift(js_text)
    print('\n>>>shift:', array_shift)

    # while True:
    #     encoded_index = int(input('encoded index: '))
    #     print(get_decoded_item(encoded_index, decoded_array, array_shift))

    # encoded_chunks = re.finditer(r'\b\w\(\d{3}\)', js_text)
    # for chunk in encoded_chunks:
    #     chunk = chunk.group()
    #     chunk_index = int(re.findall(r'\d+', chunk)[0])
    #     decoded_chunk = get_decoded_item(
    #         chunk_index, decoded_array, array_shift)
    #     print(decoded_chunk)
    #     js_text.replace(chunk, decoded_chunk)
    
    encoded_chunk_pattern = r'\b\w\(\d{3}\)'
    decoded_js_text = re.sub(
        encoded_chunk_pattern,
        lambda x: print(x.group()),
        # lambda x: get_decoded_item(x.group(), decoded_array, array_shift),
        js_text)

    with open('versions/actual_tags_decoded.js', 'w') as f:
        f.write(decoded_js_text)
            




if __name__ == '__main__':
    js_file = 'versions/actual_tags_unescaped.js'
    main(js_file)

    # print(deobfuscate('HsQSLK'))
