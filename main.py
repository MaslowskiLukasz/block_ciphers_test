
import timeit
import binascii
import terminal
import crypto

def print_hello():
  for i in range(1,1_000_000):
    print("test")

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
encrypted = crypto.encrypt_ECB(bytes_msg, key)
decrypted = crypto.decrypt_ECB(encrypted, key)


terminal.print_output(input_msg, "input")
terminal.print_output(hex_msg, "hex")
terminal.print_output(formated_output, "formated")
terminal.print_output(colored_output, "colored")
terminal.print_output(encrypted, "encrypted")
terminal.print_output(str(decrypted), "decrypted")
