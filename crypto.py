from Crypto.Cipher import AES

def encrypt_ECB(msg, key):
  aes = AES.new(key, AES.MODE_ECB)
  length = 16 - (len(msg) % 16)
  msg += bytes([length]) * length
  return aes.encrypt(msg)

def decrypt_ECB(msg, key):
  aes = AES.new(key, AES.MODE_ECB)
  decrypted = aes.decrypt(msg)
  return decrypted[:-decrypted[-1]]