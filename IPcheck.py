'''Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
IPs should be considered valid if they consist of four octets, 
with values between 0 and 255, inclusive.'''

string ="0"
def is_valid_IP(string):
    splitString = string.split(".")
    for oct in splitString:
        print(oct)
        if len(splitString) != 4:
            return False
        print(len(oct))
        if oct[0] == "0" and len(oct) >= 2:
            return False
        if oct.isnumeric():
            if int(oct) > 255:
                print("big")
                return False
        else:
            return False
    return True
check = is_valid_IP(string)
print(check)


"""
a ="192.168.24.3"
b = a.split(".")
print(b)
print(len(b))
print(b[1])
c = b[1]
print(c[1])
"""