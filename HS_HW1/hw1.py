import sys
import hashlib
from pyfinite import ffield
import ipdb

sbox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

mixbox = [2,3,1,1,1,2,3,1,1,1,2,3,3,1,1,2]

F = ffield.FField(8)

num_rows = 4
num_cols = 4

def printArr(state):
    for i in range(4):
        for j in range(4):
            print("%3d" % (state[i][j]), end=' ')
        print()

def subByte(state):
    return [[sbox[byte] for byte in word] for word in state]

def shiftRows(state):
    tmp = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for r in range(num_rows):
        for c in range(num_cols):
            tmp[r][c] = state[r][((r+c) % num_rows)]
    return tmp

def mixColumns(state):
    tmp_arr = [0 for i in range(num_rows * num_cols)]
    for r in range(num_rows):
        for c in range(num_cols):
            tmp_val = 0
            for i in range(num_cols):
                print(mixbox[r*4 + c])
                print(state[c*4 + r])
                print('a',F.Multiply(mixbox[r*4 + i], state[i*4 + r]))
                tmp_val ^= F.Multiply(mixbox[r*4 + i], state[i*4 + r])
                print('b',tmp_val)
            print('c',tmp_val)
            tmp_arr[r*4 + c] = tmp_val
    ipdb.set_trace()
    return tmp_arr


def main():
    md5_hash = hashlib.md5()
    student_id = 'b04902105'
    md5_hash.update(student_id.encode('utf-8'))
    key = md5_hash.hexdigest()
    int_key = [int(key[h:h+2], 16) for h in range(0, len(key), 2)]

    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            plaintext = line.strip().split(',')
            state_arr = [[int(w) for w in plaintext[4*i: 4*(i+1)]] for i in range(4)]
            state_arr = subByte(state_arr)
            printArr(state_arr)
            state_arr = shiftRows(state_arr)
            printArr(state_arr)
            #state_arr = mixColumns(state_arr)
            #printArr(state_arr)
            break

    b = float(sys.argv[2])
    noise = float(sys.argv[3])


if __name__ == '__main__':
    main()
