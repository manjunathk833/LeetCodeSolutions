# Python3 program for the above approach

# Function to convert Decimal to Hex
def convertToHex(num):
    temp = ""
    while (num != 0):
        rem = num % 16
        c = 0

        if (rem < 10):
            c = rem + 48
        else:
            c = rem + 87

        temp += chr(c)
        num = num // 16

    return temp


# Function to encrypt the string
def encryptString(S, N):
    ans = ""

    # Iterate the characters
    # of the string
    for i in range(N):
        ch = S[i]
        count = 0

        # Iterate until S[i] is equal to ch
        while (i < N and S[i] == ch):
            # Update count and i
            count += 1
            i += 1

        # Decrement i by 1
        i -= 1

        # Convert count to hexadecimal
        # representation
        hex = convertToHex(count)

        # Append the character
        ans += ch

        # Append the characters frequency
        # in hexadecimal representation
        ans += hex

    # Reverse the obtained answer
    ans = ans[::-1]

    # Return required answer
    return ans


# Driver Code
if __name__ == '__main__':
    # Given Input
    S = "abc"
    N = len(S)

    # Function Call
    print(encryptString(S, N))
