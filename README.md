# Cryptography
This is a programming exercise for the Cryptography Module.

# Getting started
Instructions on how to download and run the project for testing or developing purposes.

## Requirements
You have to make sure that you have Python3 and pip installed. In order to verify this you can open a terminal and type 
```bash
python -V
```
The output should be the Python version. Then you can type the following in order to check the pip version
```bash
python -m pip --version
```
The output should be the pip version.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries that the project uses, they can be found in the requirements.txt file. Open the terminal and run the following command inside the project's folder.
```bash
pip install -r requirements.txt
```

# Usage
This project consists in two different tasks. 

## Cryptography1
This project allows you to encrypt and decrypt a given text using 4 different AES encryption modes. The key is stored in a config file and the IV is randomly generated unless the -s flag is used, in which case a static IV stored in the same config file will be used.
```
Usage: main.py -t <plain text> -m <CBC|CFB|ECB|OFB> [-s]

Options:
  -h, --help  show this help message and exit
  -m MODE     AES mode [CBC|CFB|ECB|OFB]
  -t TEXT     text to cypher
  -s          static IV
```


##Cryptography2
This project allows you to hash a given file with the MD5 algorithm. The usage is very simple, the program will ask for the path and name of the file and then will show the result hash.

# AES encryption algorithm
The block ciphers are schemes for encryption or decryption where a block of plaintext is treated as a single block and is used to obtain a block of ciphertext with the same size. AES (Advanced Encryption Standard) is one of the most used algorithms for block encryption.

The size of an AES block is 128 bits, whereas the size of the encryption key can be 128, 192 or 256 bits. Block cipher algorithms should enable encryption of the plaintext with size which is different from the defined size of one block as well. Padding algorithms can be used when the plaintext is not enough a block.

## ECB Mode
The ECB (Electronic Code Book) mode is the simplest of all. The plaintext is divided into blocks as the length of the block of AES, 128. So the ECB mode needs to pad data until it is same as the length of the block. Then every block will be encrypted with the same key and same algorithm. So if you encrypt the same plaintext, you will get the same ciphertext.

Encryption:
![ECB Encryption](https://highgo.ca/wp-content/uploads/2019/08/ECB-encryption-1024x408.png)

Decryption:
![ECB Decryption](https://highgo.ca/wp-content/uploads/2019/08/ECB-Decryption-1024x408.png)

## CBC Mode
The CBC (Cipher Block Chaining) mode provides this by using an initialization vector (IV). The IV has the same size as the block that is encrypted. The plaintext is divided into blocks and needs to add padding data. First, the plaintext block will xor with the IV. Then CBC will encrypt the result to the ciphertext block. In the next block, the encryption result to xor will be used with plaintext block until the last block. In this mode, even if the same plaintext block ins encrypted, the result will be a different ciphertext block. If a plaintext or ciphertext block is broken, it will affect all following block.

Encryption:
![CBC Encryption](https://highgo.ca/wp-content/uploads/2019/08/CBC-encryption-1024x408.png)

Decryption:
![CBC Decryption](https://highgo.ca/wp-content/uploads/2019/08/CBC-Decryption-1024x411.png)

## CFB Mode
The CFB (Cipher FeedBack) mode of operation allows the block encryptor to be used as a stream cipher. It also needs an IV. First, CFB will encrypt the IV, then it will xor with plaintext block to get ciphertext. Then we will encrypt the encryption result to xor the plaintext. Because this mode will not encrypt plaintext directly, it just uses the ciphertext to xor with the plaintext to get the ciphertext. So in this mode, it doesn’t need to pad data.

Encryption:
![CFB Encryption](https://highgo.ca/wp-content/uploads/2019/08/CFB-encryption-1024x288.png)

Decryption:
![CFB Decryption](https://highgo.ca/wp-content/uploads/2019/08/CFB-Decryption-1024x288.png)

## OFB Mode
The OFB (Output FeedBack) mode of operation also enables a block encryptor to be used as a stream encryptor. It also doesn't need padding data. In this mode, it will encrypt the IV in the first time and encrypt the per-result. Then it will use the encryption results to xor the plaintext to get ciphertext. It is different from CFB, it always encrypts the IV. It will not be affected by the broken block.

Encryption:
![OFB Encryption](https://highgo.ca/wp-content/uploads/2019/08/OFB-encryption-1024x516.png)

Decryption:
![OFB Decryption](https://highgo.ca/wp-content/uploads/2019/08/OFB-Decryption-1024x517.png)


Resources: https://www.highgo.ca/2019/08/08/the-difference-in-five-modes-in-the-aes-encryption-algorithm/

# Built with
* [PyCharm Professional 2021.1](https://www.jetbrains.com/pycharm/) - Python IDE
* [Python 3.7.4](https://www.python.org/) - Programming language

# Author
* **Lucrecia Amenta** - *Initial work* - [Seraffina-93](https://github.com/Seraffina-93)
