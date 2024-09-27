# last char is missed in this solver


def base64_decode(encoded_str):
    # Base64 alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
    
    result = ''
    temp = 0
    bit_count = 0
    
    for char in encoded_str:
        if char == '=':
            break
        
        idx = alphabet.index(char)
        
        temp |= idx << (18 - bit_count * 6)
        bit_count += 1
        
        if bit_count == 4:
            result += chr((temp >> 16) & 0xFF)
            result += chr((temp >> 8) & 0xFF)
            result += chr(temp & 0xFF)
            
            temp = 0
            bit_count = 0
    
    # Handle remaining bytes
    if bit_count > 1:
        result += chr((temp >> 10) & 0xFF)
    if bit_count > 2:
        result += chr((temp >> 2) & 0xFF)
    
    return result

# Example usage
encoded_strings = ["z2v0tw91C2vqB3nPDgLVBG", "CgfYzw50rwXLBwvUDa", "zgf0yurVBwvxB3jRzxjfDMvUDe5HBwu", "sfrntfzPzgvVrwXLBwvUDa", "neuXnZLbnZmXmeneouiYmZqWrJG1rdKXoee5nKm4"]
for i in encoded_strings:
    print(f"Encoded: {i}")
    decoded_result = base64_decode(i)
    print(f"Decoded: {decoded_result}\n")

