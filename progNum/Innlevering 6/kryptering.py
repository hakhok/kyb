"""Oppgave: Kryptering. Innlevering 6"""

import binascii
from random import randint

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(word, key):
    if len(word) == len(key):
        word = toHex(bytes(word, encoding = 'ascii'))
        key = toHex(bytes(key, encoding = 'ascii'))

        code = word^key
        return code

    print("Length of word and key does not match")
    return 0

def decrypt(code, key):
    key = toHex(bytes(key, encoding = 'ascii'))
    word = toString(code^key)
    return word

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def main():
    sentence = input("Hva er meldingen? ")
    key = str(random_with_N_digits(len(sentence)))
    code = encrypt(sentence, key)
    decrypted_sentence = decrypt(code, key)
    print(f"Krypto: {key}")
    print(f"Melding: {decrypted_sentence}")

main()
