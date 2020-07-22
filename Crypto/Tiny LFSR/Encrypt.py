import sys
from binascii import unhexlify

if(len(sys.argv)<4):
	print("Usage: python Encrypt.py keyfile plaintext ciphername")
	exit(1)

def lfsr(R, mask):
	output = (R << 1) & 0xffffffffffffffff
	i=(R&mask)&0xffffffffffffffff
	lastbit=0
	while i!=0:
		lastbit^=(i&1)
		i=i>>1
	output^=lastbit
	return (output,lastbit)

R = 0
key = ""
with open(sys.argv[1],"r") as f:
	key = f.read()
	R = int(key,16)
	f.close
	
mask = 0b1101100000000000000000000000000000000000000000000000000000000000

a = ''.join([chr(int(b, 16)) for b in [key[i:i+2] for i in range(0, len(key), 2)]])

f=open(sys.argv[2],"r")
ff = open(sys.argv[3],"wb")
s = f.read()
f.close()
lent = len(s)

for i in range(0, len(a)):
	ff.write((ord(s[i])^ord(a[i])).to_bytes(1, byteorder='big'))

for i in range(len(a), lent):
    tmp=0
    for j in range(8):
        (R,out)=lfsr(R,mask)
        tmp=(tmp << 1)^out
    ff.write((tmp^ord(s[i])).to_bytes(1, byteorder='big'))
ff.close()


