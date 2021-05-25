from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

from cryptography.hazmat.primitives import padding

# ECB (Electronic Code Book) is the simplest mode of operation for block ciphers.
# Each block of data is encrypted in the same way.
# This means identical plaintext blocks will always result in identical ciphertext blocks,
# which can leave significant patterns in the output.

# Padding is required when using this mode.
# ECB does not use iv


def encrypt(key, plaintext):
    # Construct an AES-ECB Cipher object with the given key
    encryptor = Cipher(
        algorithms.AES(key),
        modes.ECB(),
    ).encryptor()

    # padding data
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Encrypt the plaintext and get the associated ciphertext.
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext


def decrypt(key, ciphertext):
    # Construct a Cipher object, with the key
    decryptor = Cipher(
        algorithms.AES(key),
        modes.ECB(),
    ).decryptor()

    # remove padding
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    output = unpadder.update(padded_data) + unpadder.finalize()

    # Decryption gets the authenticated plaintext.
    return output

# For testing just this file
# ciphertext = encrypt(
#     key,
#     plaintext
# )

# print(ciphertext)

# print(decrypt(
#     key,
#     ciphertext
# ))