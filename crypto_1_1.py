import binascii
import codecs

hexStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

rawBytes = binascii.unhexlify(hexStr)

b64Data = codecs.encode(rawBytes, 'base64')

print(b64Data)
