#
# name = input()                  # Reading input from STDIN
# print('Hi,', name)         # Writing output to STDOUT
#
# n = len(name)
# b = int(n/2)
# for i in range(b):
#     print(n - i)
#     if name[i] != name[n-i-1]:
#
#         f = 0
#         break
#     elif name[i] == name[n-i-1]:
#         f = 1
#
# if f == 1:
#     if n%2 == 0:
#         print("EVEN PALINDROME")
#     else:
#         print("ODD PALINDROME")
# else:
#     print("NOT A PALINDROME")

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT


n = len(name)

str = list(name)
for i in range(n):
    if str[i].isupper():
        str[i] = str[i].lower()
    elif str[i].islower():
        str[i] = str[i].upper()

name = ''.join(str)
print(name)