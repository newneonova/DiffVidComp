import os, zlib,  io
Dir = 'JellyOut/'
Images=list()
D=list()
for file in os.listdir(Dir):
    with open(Dir+file,'rb') as imageFile:
        f = imageFile.read()
        b=bytearray(f)
        Images.append(b)
if not os.path.exists('DiffOut'):
    os.makedirs('DiffOut')
OldIm = Images[0]
count=0
for i in range(1,len(Images)):
    print(str(count))
    with open("DiffOut/"+str(count)+".bmp", "wb") as f:
        f.write(OldIm)


    count=count+1
    Z=bytearray()
    for j in range(len(Images[i])):
        if(j<(14+7+16)):
            Z.append(Images[i-1][j])
        else:
            Z.append(Images[i-1][j]^Images[i][j])
    OldIm = Z
with open("DiffOut/"+str(count)+".bmp", "wb") as f:
    f.write(OldIm)
    

