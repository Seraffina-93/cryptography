from cryptography.hazmat.primitives.hashes import Hash

from cryptography.hazmat.primitives.hashes import MD5

from termcolor import colored

digest = Hash(MD5())

input_file = input(colored("[+] Insert the path & name of the file you want to hash: \n", 'blue'))
print(colored("Hashing file with MD5 algorithm...", 'blue'))
executable = open(input_file, "rb")
digest.update(executable.read())
out = digest.finalize()
decoded = out.hex()
print(colored("[!!] Hash result: " + decoded, 'green'))

# WinMD5.exe hash:
# 944a1e869969dd8a4b64ca5e6ebc209a

# WiiniMD5_2.exe hash:
# d1284c8060db2d9e8960696b6b8ccfc4

