#�� -*- coding:utf-8 -*-
flag = ''
f = open('flag.txt','r')
input = f.readline()
assert input.startswith('afctf{')
assert input.endswith('}')
flag = input[6:21]
f.close()
print input + flag

def enc1(word, i):
        word = ord(word) ^ 0x76 ^ 0xAD
        temp1 = (word & 0xAA) >> 1
        temp2 = 2 * word & 0xAA
        word = temp1 | temp2
        return word

def enc2(word, i):        
        word = ord(word) ^ 0x76 ^ 0xBE
        temp1 = (word & 0xCC) >> 2
        temp2 = 4 * word & 0xCC
        word = temp1 | temp2
        return word


def enc3(word,i):
        word = ord(word) ^ 0x76 ^ 0xEF
        temp1 = (word & 0xF0) >> 4
        temp2 = 16 * word & 0xF0
        word = temp1 | temp2
        return word 
		
output = ''

for i in range(5):
	output += chr(enc1(flag[i],i))

for i in range(5):
	output += chr(enc2(flag[i+5],i))
	
for i in range(5):
	output += chr(enc3(flag[i+10],i))
	
f = open('output','w')
f.write(output)
f.close()
