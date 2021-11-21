
import timeit
import binascii
import terminal
import crypto
import files

def ECB_encrypt(bytes_msg):
  if len(bytes_msg) % 16 != 0:
    bytes_msg = crypto.add_padding(bytes_msg)
  encrypted = crypto.encrypt_ECB(bytes_msg, key)
  terminal.print_output(encrypted, "encrypted ECB")
  files.save_to_file("output/", "ECB_en_"+file_name, encrypted)

def ECB_decrypt(bytes_msg):
  if len(bytes_msg) % 16 != 0:
    bytes_msg = crypto.add_padding(bytes_msg)
  decrypted = crypto.decrypt_ECB(bytes_msg, key)
  terminal.print_output(decrypted[:-decrypted[-1]], "decrypted ECB")
  files.save_to_file("output/", "ECB_de_"+file_name, decrypted)

def CBC_encrypt(bytes_msg):
  if len(bytes_msg) % 16 != 0:
    bytes_msg = crypto.add_padding(bytes_msg)
  encrypted = crypto.encrypt_CBC(bytes_msg, key, iv)
  terminal.print_output(encrypted, "encrypted CBC")
  files.save_to_file("output/", "CBC_en_"+file_name, encrypted)

def CBC_decrypt(bytes_msg):
  if len(bytes_msg) % 16 != 0:
    bytes_msg = crypto.add_padding(bytes_msg)
  decrypted = crypto.decrypt_CBC(bytes_msg, key, iv)
  terminal.print_output(decrypted[:-decrypted[-1]], "decrypted CBC")
  files.save_to_file("output/", "CBC_de_"+file_name, decrypted)

terminal.print_modes()
mode = int(input("Select mode: "))
print(mode)
path = terminal.print_files(mode)
file_name = input("Choose a file: ")
bytes_msg = files.read_as_bytes(path, file_name)

key = b"rick astley goat"
iv = b"asfir34qgbtr834g"

terminal.print_output(bytes_msg, "input")
if mode == 1:
  time = timeit.timeit(lambda: ECB_encrypt(bytes_msg), number=1)
  print(time)
elif mode == 2:
  time = timeit.timeit(lambda: ECB_decrypt(bytes_msg), number=1)
  print(time)
elif mode == 3:
  time = timeit.timeit(lambda: CBC_encrypt(bytes_msg), number=1)
  print(time)
elif mode == 4:
  time = timeit.timeit(lambda: CBC_decrypt(bytes_msg), number=1)
  print(time)
else:
  print("Wrong mode")



