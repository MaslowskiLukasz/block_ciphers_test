
import timeit
import binascii
import terminal
import crypto

def read_from_file(file_name):
  with open(f"input/{file_name}", "r") as file:
    text = file.read()
  return text

#time = timeit.timeit(print_hello, number=1)
#print(time)

block_length = 8
input_msg = read_from_file("rick_roll.txt")
bytes_msg = bytes(input_msg, 'utf-8')
hex_msg = binascii.hexlify(bytes_msg)
formated_output = terminal.format_output(str(hex_msg)[2:-1], block_length)
colored_output = terminal.color(formated_output)

key = b"rick astley goat"
iv = b"asfir34qgbtr834g"
bytes_msg = crypto.add_padding(bytes_msg)

encrypted = crypto.encrypt_ECB(bytes_msg, key)
decrypted = crypto.decrypt_ECB(encrypted, key)
encrypted_CBC = crypto.encrypt_CBC(bytes_msg, key, iv)
decrypted_CBC = crypto.decrypt_CBC(encrypted_CBC, key, iv)

terminal.print_output(input_msg, "input")
terminal.print_output(encrypted, "encrypted ECB")
terminal.print_output(decrypted[:-decrypted[-1]], "decrypted ECB")
terminal.print_output(encrypted_CBC, "encrypted CBC")
terminal.print_output(decrypted_CBC[:-decrypted_CBC[-1]], "decrypted CBC")