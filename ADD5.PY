
some_bytes = b'\xC3\xA9'  
with open("my_file.txt", "wb") as binary_file:
    binary_file.write(some_bytes)
