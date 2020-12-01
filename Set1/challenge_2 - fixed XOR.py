# Challenge 2: Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:
#             1c0111001f010100061a024b53535009181c

# ... after hex decoding, and when XOR'd against:
#
#             686974207468652062756c6c277320657965

# ... should produce:
#
#             746865206b696420646f6e277420706c6179

from binascii import hexlify, unhexlify

input_string_1 = '1c0111001f010100061a024b53535009181c'
input_bytes_2 = '686974207468652062756c6c277320657965'

# This is the same as unhexlify
# binary2 = bytes.fromhex(input_bytes)


string_bytes = unhexlify(input_string_1)  # returns: b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'
string_bytes2 = unhexlify(input_bytes_2)  # returns: b"hit the bull's eye"


def xor_byte_strings(input_a, input_b):
    byte_list = bytes([a ^ b for a, b in zip(input_a, input_b)])
    return hexlify(byte_list)


xor_byte_strings(string_bytes, string_bytes2)  # returns: 746865206b696420646f6e277420706c6179 <---- Correct answer!

# unhexlify(xor_byte_strings(string_bytes, string_bytes2)  #returns: b"the kid don't play"
