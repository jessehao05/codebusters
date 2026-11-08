
# encode: 
#     - offset of 3: a --> d
#     - go through each letter and add offset
#     - if not a letter, then skip

# decode:
#     - if key known:
#         - go through each letter and subtract the offset
#         - if not a letter, then skip
#     - if key not known:
#         - iterate for all offsets (1 - 26) and repeat steps above until human readable text is the output

def encode_ceasar(input: str, key: int) -> str:
    """Encodes a ceasar cipher given a string and a key."""

    output = []

    for char in input:
        if not char.isalpha():
            output.append(char)
        else:

            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))

            output.append(encoded_char)

    return "".join(output)

def decode_ceasar_key(input: str, key: int) -> str:
    """Decodes a caesar cipher given a string and a key."""

    output = []
    
    for char in input:
        if not char.isalpha():
            output.append(char)
        else:

            if char.isupper():
                decoded_har = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            if char.islower():
                decoded_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))

            output.append(decoded_char)

    return "".join(output)


def decode_ceasar_no_key(input: str) -> str:
    """Decodes a caesar cipher given a string."""

    res = ""

    for i in range(1, 26):
    
        output = []
        
        for char in input:
            if not char.isalpha():
                output.append(char)
            else:

                if char.isupper():
                    decoded_har = chr((ord(char) - ord('A') - i) % 26 + ord('A'))
                if char.islower():
                    decoded_char = chr((ord(char) - ord('a') - i) % 26 + ord('a'))

                output.append(decoded_char)

        decoded_str = "".join(output)
        res += f"Offset of {i}: " + decoded_str + "\n"

    return res


print(encode_ceasar("Hello WoRLD!", 3))
print(decode_ceasar_key("khoor zruog!", 3))
print(decode_ceasar_no_key("khoor zrong!"))