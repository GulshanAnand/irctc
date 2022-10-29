# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)
import hashlib

# initializing string
#str2hash = "123456"

# encoding GeeksforGeeks using encode()
# then sending to md5()

#result = hashlib.md5(str2hash.encode())

#val = result.hexdigest()
#print(val)
#print(type(val))

def encrypt(str):
	result = hashlib.md5(str.encode()).hexdigest()
	return result