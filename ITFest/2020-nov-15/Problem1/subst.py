import base64
import sys
from pathlib import Path
from subprocess import check_output

alphabet = bytes(range(32, 128)) + b'\n\r'
Path('alphabet.bin').write_bytes(alphabet)
alphabet_encoded = base64.b64decode(check_output('ctf1.exe -c alphabet.bin'))

reverse_cipher = {}
for idx, encoded in enumerate(alphabet_encoded):
    if idx < len(alphabet):
        reverse_cipher[encoded] = alphabet[idx]

ciphertext = base64.b64decode(Path(sys.argv[1]).read_bytes())

decoded = bytearray()
for e in ciphertext:
    decoded.append(reverse_cipher[e])

print(decoded.decode('utf-8'))
