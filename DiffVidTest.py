import os, zlib
Dir = 'JellyOut/'
Images=list()
D=list()
for file in os.listdir(Dir):
    with open(Dir+file,'rb') as imageFile:
        f = imageFile.read()
        b=bytearray(f)
        Images.append(b)
D.append(Images[0])
count=0
for i in range(1,len(Images)):
    print(count)
    count=count+1
    Z=bytearray()
    for j in range(len(Images[i])):
        Z.append(Images[i-1][j]^Images[i][j])
    D.append(Z)
C = list()
for H in D:
    I = int.from_bytes(H,byteorder='big')
    
    C.append(zlib.compress(H))
Z = bytearray()
for H in C:
    Z.append(H)

open('CMP.zlz','w').write(Z)
    
C = list()
for H in Images:
    C.append(zlib.compress(H))
for H in C:
    Z.append(H)
open('BAD.zlz','w').write(Z)
