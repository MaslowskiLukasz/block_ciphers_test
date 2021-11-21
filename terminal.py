from termcolor import colored
import os

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

def print_output(text, title):
  print(title)
  print("###")
  print(text)
  print("----------------------------------------")

def print_modes():
  print("1. Encrypt ECB")
  print("2. Decrypt ECB")
  print("3. Encrypt CBC")
  print("4. Decrypt CBC")

def print_files(mode):
  if mode % 2 == 0:
    print(os.listdir("output/"))
    return "output/"
  else:
    print(os.listdir("input/"))
    return "input/"