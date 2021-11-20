from termcolor import colored

def format_output(data, block_length):
  return ' '.join(data[i:i+block_length] for i in range(0,len(data),block_length))

def color(text):
  arr = text.split(" ")
  output = ""
  for i in range(0, len(arr)):
    if i % 2 == 0:
      output += colored(arr[i], "cyan") + " "
    else:
      output += colored(arr[i], "green") + " "
  return output

def print_output(text, title):
  print(title)
  print("###")
  print(text)
  print("----------------------------------------")