from Crypto.Cipher import AES

def add_padding(msg):
  length = 16 - (len(msg) % 16)
  msg += bytes([length]) * length
  return msg

def encrypt_ECB(msg, key):
  aes = AES.new(key, AES.MODE_ECB)
  encrypted = aes.encrypt(msg)
  return encrypted

def decrypt_ECB(msg, key):
  aes = AES.new(key, AES.MODE_ECB)
  return aes.decrypt(msg)

def xor(current, previous):
  return bytes(a ^ b for a, b in zip(current, previous))

def encrypt_CBC(msg, key, init_vector):
  output = b""
  previous_block = init_vector
  for i in range(0, len(msg), 16):
    current_block = msg[i:i+16]
    encrypted_block = encrypt_ECB(xor(current_block, previous_block), key)
    output += encrypted_block
    previous_block = encrypted_block
  return output

def decrypt_CBC(msg, key, init_vector):
  output = b""
  previous_block = init_vector
  for i in range(0, len(msg), 16):
    current_block = msg[i:i+16]
    output += xor(decrypt_ECB(current_block, key), previous_block)
    previous_block = current_block
  return output

def encrypt_PBC(msg, key, init_vector):
  output = b""
  previous_block = init_vector
  for i in range(0, len(msg), 16):
    current_block = msg[i:i+16]
    encrypted_block = encrypt_ECB(xor(current_block, previous_block), key)
    output += encrypted_block
    previous_block = current_block
  return output

def decrypt_PBC(msg, key, init_vector):
  output = b""
  previous_block = init_vector
  for i in range(0, len(msg), 16):
    current_block = msg[i:i+16]
    decrypted = xor(decrypt_ECB(current_block, key), previous_block)
    output += decrypted
    previous_block = decrypted
  return output