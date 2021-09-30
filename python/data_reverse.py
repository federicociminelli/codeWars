'''
Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)

should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
 
The total number of bits will always be a multiple of 8.
'''

def data_reverse(data):
    return sum([data[i:i+8] for i in range(0, len(data), 8)][::-1], [])

