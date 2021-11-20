from Crypto.Cipher import AES
from termcolor import colored
import timeit
import binascii

def print_hello():
  for i in range(1,1_000_000):
    print("test")

def read_from_file(file_name):
  with open(f"input/{file_name}", "r") as file:
    text = file.read()
  return text

def format_output(data, block_length):
  return ' '.join(data[i:i+block_length] for i in range(0,len(data),block_length))
  

def color(text):
  arr = text.split(" ")
  output = ""
  for i in range(0, len(arr)):
    if i % 2 == 0:
      output += colored(arr[i], "red") + " "
    else:
      output += colored(arr[i], "green") + " "
  return output
    

#time = timeit.timeit(print_hello, number=1)
#print(time)

block_length = 8
input_msg = read_from_file("rick_roll.txt")
print(input_msg)
print("------------------------------------------")
bytes_msg = bytes(input_msg, 'utf-8')
hex_msg = binascii.hexlify(bytes_msg)
print(hex_msg)
print("------------------------------------------")
formated_output = format_output(str(hex_msg)[2:], block_length)
print(formated_output)
print("------------------------------------------")
print(color(formated_output))