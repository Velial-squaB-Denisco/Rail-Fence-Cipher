import numpy as np

def encode_rail_fence_cipher(string, n):

    string = list(string)

    matrix = np.full((n, len(string)), '', dtype=str)

    j = 0
    d = 1

    for i in range(len(string)):
        matrix[j][i] = string[i]

        if j == n - 1:
            d = -1
        elif j == 0:
            d = 1

        j += d

    print(matrix)
    res = ""
    for i in range(n):
        res += "".join(matrix[i])
    
    return res
    
def decode_rail_fence_cipher(string, n):

    #//////
    matrix = np.full((n, len(string)), '', dtype=str)
    j = 0
    d = 1

    for i in range(len(string)):
        matrix[j][i] = '*'

        if j == n - 1:
            d = -1
        elif j == 0:
            d = 1

        j += d

    index = 0
    for i in range(n):
        for j in range(len(string)):
            if matrix[i][j] == '*':
                matrix[i][j] = string[index]
                index += 1

    res = ""
    j = 0
    d = 1
    for i in range(len(string)):
        res += matrix[j][i]

        if j == n - 1:
            d = -1
        elif j == 0:
            d = 1

        j += d

    return res
    
    #//////

print(encode_rail_fence_cipher("Hello, World!", 4))

print(decode_rail_fence_cipher(encode_rail_fence_cipher("Hello, World!", 4), 4))
