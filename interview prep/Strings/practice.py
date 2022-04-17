

def reverse_words(str, start, end):
    while start < end:
        str[start], str[end] = str[end], str[start]
        start = start + 1
        end = end - 1
    return

s = "Hello there this is a string"

str = list(s)

start = 0
l = len(str)

try:
    while start < l:
        end = str.index(" ", start)
        reverse_words(str, start, end-1)
        start = end + 1
except:
    reverse_words(str, start, l-1)

str.reverse()

s = "".join(str)

print("reversed words are ", s)


