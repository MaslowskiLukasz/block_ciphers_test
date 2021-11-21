def read_from_file(path, file_name):
  with open(f"{path}{file_name}", "r") as file:
    text = file.read()
  return text

def save_to_file(path, file_name, data):
  with open(f"{path}{file_name}", "wb") as file:
    file.write(data)

def read_as_bytes(path, file_name):
  with open(f"{path}{file_name}", "rb") as file:
    input_bytes = file.read()
  return input_bytes