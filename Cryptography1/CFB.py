from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

# CFB (Cipher Feedback) is a mode of operation for block ciphers.
# It transforms a block cipher into a stream cipher.
# This mode does not require padding.


def encrypt(key, plaintext, iv):
    # Construct an AES-CFB Cipher object with the given key and IV
    encryptor = Cipher(
        algorithms.AES(key),
        modes.CFB(iv),
    ).encryptor()

    # Encrypt the plaintext and get the associated ciphertext.
    # CFB does not require padding.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext


def decrypt(key, iv, ciphertext):
    # Construct a Cipher object, with the key and iv
    decryptor = Cipher(
        algorithms.AES(key),
        modes.CFB(iv),
    ).decryptor()

    # Decryption gets us the authenticated plaintext.
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
