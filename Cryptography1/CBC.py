from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

from cryptography.hazmat.primitives import padding

# CBC (Cipher Block Chaining) is a mode of operation for block ciphers.
# It is considered cryptographically strong.
# Padding is required when using this mode.


def encrypt(key, plaintext, iv):
    # Construct an AES-CBC Cipher object with the given key and IV
    encryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
    ).encryptor()

    # padding data
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Encrypt the plaintext and get the associated ciphertext.
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext


def decrypt(key, iv, ciphertext):
    # Construct a Cipher object, with the key and iv
    decryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
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
#     plaintext,
#     iv
# )
#
# print("Ciphertext: ", ciphertext)
#
# print(decrypt(
#     key,
#     iv,
#     ciphertext
# ))
