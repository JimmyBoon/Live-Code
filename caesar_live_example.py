# Caesar Cipher:
#
# Write a program that can encode and decode, using the Caesar Cipher method.
# https://en.wikipedia.org/wiki/Caesar_cipher
# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/pi/caesar-cipher-exploration

# Basically we encode a string by changing its position be a certain value
# and decode it by moving back by that value.

# For example: "my house" adjusted by 1, will be "nz ipvtf"

# Plan for the program:
# A: Encoding:
# 1. Convert the letters to numbers
# 2. Add a adjustment value to the number
# 3. Turn the number back into text.

# B: Decoding
# 1. Convert the letters to numbers
# 2. Minus a adjustment value to the number
# 3. Turn the number back into text.

# Plan on how to code:
# 1. Plan
# 2. Development
# 3. Test
# 4. Deploy

# Variables:
text_to_be_encoded = "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, \
Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. \
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter \
some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be \
replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it \
in his private correspondence."

# ---------- Demonstration workings: ----------

# A: Encoding:
# 1. Convert the letters to numbers:

# print(ord("a"))
# print(ord("b"))
# print(ord(" "))

# text_to_numbers = []
# adjustment = 1

# 2. Add a adjustment value to the number

# for characters in text_to_be_encoded:
#     text_to_numbers.append((ord(characters) + adjustment) % 128)

# # print(ord("a"))
# # print(chr(97))
# # print(chr(98))

# 3. Turn the number back into text.

# encoded_text_list = []

# for number in text_to_numbers:
#     encoded_text_list.append(chr(number))

# encoded_text = "".join(encoded_text_list)

# ------------------------------




def encode(text_to_be_encoded, adjustment):
    """Function for encoding the text, takes a string to be encoded, and a adjustment for the encoding.
    """
    text_to_numbers = []

    for characters in text_to_be_encoded:
        text_to_numbers.append((ord(characters) + adjustment) % 128)

    encoded_text_list = []

    for number in text_to_numbers:
        encoded_text_list.append(chr(number))
    
    encoded_text = "".join(encoded_text_list)

    return encoded_text


def decode(text_to_be_decoded, adjustment):
    """Function for decoding the text, takes a string to be decoded, and a adjustment for the decoding.
    """
    adjustment = -adjustment
    decoded_text = encode(text_to_be_decoded, adjustment)
    return decoded_text

encoded_text_test = encode(text_to_be_encoded, 1)
print(encoded_text_test)


decoded_text_test = decode(encoded_text_test, 1)
print(decoded_text_test)


