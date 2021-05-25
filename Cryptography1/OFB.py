from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

# OFB (Output Feedback) is a mode of operation for block ciphers.
# It transforms a block cipher into a stream cipher.
# Padding is not required when using this mode.


def encrypt(key, plaintext, iv):
    # Construct an AES-OFB Cipher object with the given key and IV
    encryptor = Cipher(
        algorithms.AES(key),
        modes.OFB(iv),
    ).encryptor()

    # Encrypt the plaintext and get the associated ciphertext.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext


def decrypt(key, iv, ciphertext):
    # Construct a Cipher object, with the key and iv
    decryptor = Cipher(
        algorithms.AES(key),
        modes.OFB(iv),
    ).decryptor()

    # Decryption gets the authenticated plaintext.
    return decryptor.update(ciphertext) + decryptor.finalize()

# For testing just this file
# ciphertext = encrypt(
#     key,
#     plaintext,
#     iv
# )

# print(ciphertext)
#
# print(decrypt(
#     key,
#     iv,
#     ciphertext
# ))
