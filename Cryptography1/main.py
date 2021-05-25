import os
from optparse import OptionParser

from termcolor import colored

import CBC
import CFB
import ECB
import OFB
import config
import loader

key = config.key


def main():
    usage = "usage: %prog -t <plain text> -m <CBC|CFB|ECB|OFB> [-s]"
    parser = OptionParser(usage=usage)
    parser.add_option('-m', dest='mode', type='string', help='AES mode [CBC|CFB|ECB|OFB]')
    parser.add_option('-t', dest='text', type='string', help='text to cipher')
    parser.add_option('-s', action='store_true', help='static IV')
    (options, args) = parser.parse_args()

    if options.text is None:
        parser.error(colored("[!!] Incorrect number of arguments", 'red'))
    # else:
    plain_text = options.text
    encoded_text = plain_text.encode()
    byte_text = bytearray(encoded_text)

    # sets the cryptography mode
    # mode = options.mode
    if options.mode is None:
        parser.error(colored("[!!] Please select a cryptography mode", 'red'))
    # else:
    mode = options.mode.upper()

    if options.s:
        iv_msg = "Using static IV..."
        iv = config.static_iv
    else:
        iv_msg = "Using dynamic IV..."
        iv = os.urandom(16)

    if mode == "CBC":
        cipher_text = CBC.encrypt(key, byte_text, iv)
        decrypted_text = CBC.decrypt(key, iv, cipher_text)
    elif mode == "OFB":
        cipher_text = OFB.encrypt(key, byte_text, iv)
        decrypted_text = OFB.decrypt(key, iv, cipher_text)
    elif mode == "ECB":
        cipher_text = ECB.encrypt(key, byte_text)
        decrypted_text = ECB.decrypt(key, cipher_text)
    elif mode == "CFB":
        cipher_text = CFB.encrypt(key, byte_text, iv)
        decrypted_text = CFB.decrypt(key, iv, cipher_text)
    else:
        parser.error(colored("[!!] Invalid cryptography mode", 'red'))

    print(colored("Text to encrypt: " + plain_text, 'blue'))
    print(colored("Using AES cryptography mode: " + mode, 'blue'))
    if mode == "ECB":
        print(colored("ECB does not use IV...", 'blue'))
    else:
        print(colored(iv_msg, 'blue'))

    loader.loading()

    print("\n")

    cipher_text = cipher_text.hex()
    decrypted_text = decrypted_text.decode()
    print(colored("[+] Encrypted text: " + cipher_text, 'green'))
    print(colored("[+] Decrypted text: " + decrypted_text, 'green'))


if __name__ == '__main__':
    main()
