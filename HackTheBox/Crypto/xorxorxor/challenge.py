#!/usr/bin/python3

'''
To solve this challenge you need to know some part of encrypted text and guessing one by one, when you have the 4 bytes. BOomm you got the flag

flag: HTB{rep34t3d_x0r_n0t_s0_s3cur3}'
'''

import os
flag = open('flag.txt', 'r').read().strip().encode()

class XOR:
    def __init__(self):
        self.key = b'[\x1e\xb4\x9a'
        #self.key : bytes = os.urandom(1)
    def encrypt(self, data: bytes) -> bytes:
        #print(self.key)
        xored = b''
        for i in range(len(data)):
            #print(f" {i} - {data[i]}")
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    for i in range(99999):
        crypto = XOR()
        dec_from_hex = bytes.fromhex(crypto.decrypt(bytes.fromhex(flag.decode('UTF-8'))).hex())#.decode('UTF-8')
        print(f"Using key: {crypto.key}")#, end="", flush=True)
    #'htb' in dec_from_hex or 'HTB' in dec_from_hex or
        if  b'{' in dec_from_hex : #or crypto.key == b'\x92\x1f8\x97':
            print ('Flag decoded:', dec_from_hex )
            break
            
if __name__ == '__main__':
    main()
