import base64
import sys
from pathlib import Path
from subprocess import check_output


def get_ciphertext(text):
    Path('alphabet.bin').write_bytes(text)
    encoded = check_output('ctf1.exe -x alphabet.bin')[:-2]  # remove trailing \n\r
    encoded = base64.b64decode(encoded)
    assert len(encoded) <= len(text) + 2  # might be padded to multiple of 3
    return encoded[:len(text)]


def generate(alphabet):
    for l in range(1, len(alphabet) + 1):
        test = alphabet[:l]
        alphabet_encoded = get_ciphertext(test)
        print(f'{test.decode()} -> {alphabet_encoded.decode()} -> {[x for x in base64.b64decode(alphabet_encoded)]}')


# generate(bytes(range(ord('a'), ord('z') + 1)))
# generate(b'a' * 8)
# generate(b'b' * 8)
# generate(b'c' * 8)
# generate(b'd' * 8)
# generate(b'e' * 8)
# generate(b'abcd' * 8)

reverse_ciphers = [
    {},
    {},
    {},
    {},
]

def get_ciphers_for_char(c: int):
    encoded = get_ciphertext(bytes([c] * 4))
    assert len(encoded) == 4, f'invalid? {c} {repr(chr(c))} {encoded}'
    for idx, e in enumerate(encoded):
        assert e not in reverse_ciphers[idx]
        reverse_ciphers[idx][e] = c

for c in range(32, 128):
    get_ciphers_for_char(c)

get_ciphers_for_char(ord('\n'))

def decode(ciphertext):
    result = bytearray()
    for idx, e in enumerate(ciphertext):
        result.append(reverse_ciphers[idx % 4].get(e, 32))

    return result.decode()


data = base64.b64decode(Path(sys.argv[1]).read_bytes()[:-2])
print(decode(data))
