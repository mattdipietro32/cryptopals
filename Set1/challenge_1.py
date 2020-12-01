# Challenge 1 -- Convert hex to base64

from binascii import unhexlify
from base64 import b64encode

# string:
hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'


# output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

# solution:
def hex_to_b64(hex):
    unhexed = unhexlify(hex)
    return b64encode(unhexed)
