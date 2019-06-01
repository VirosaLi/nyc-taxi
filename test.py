from hashlib import md5

print(md5('0'.encode()).hexdigest().upper())

