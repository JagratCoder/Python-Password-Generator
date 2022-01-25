import string
import random

# if __name__ == "__main__":
s1 = string.ascii_letters
# print(
s2 = string.ascii_uppercase
    # print(s2)
s3 = string.digits
    # print(s3)
s4 = string.punctuation
    # print(s4)
plen = int(input("Enter Password Length : "))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
# print(s)
print("".join(s[0:plen]))

# fps = s[0:plen]
# print(str(fps))
# print(type(fps))