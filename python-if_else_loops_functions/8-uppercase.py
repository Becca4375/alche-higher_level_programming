#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # a–z
            result += chr(ord(char) - 32)        # convert to A–Z
        else:
            result += char
    print("{}".format(result))
