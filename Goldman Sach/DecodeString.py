str = input("Enter String:")
str_encode = str.encode('utf8')
print("The encoded string in base64 format is : ",)
print(str_encode)
print("The decoded string is : ",)
print(str_encode.decode('utf8', 'strict'))
