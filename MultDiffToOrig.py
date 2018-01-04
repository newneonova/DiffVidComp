import os, zlib,  io, concurrent.futures

def MakeOrig(i,FILENAMESs,Dir):
    print(str(i))
    try:
        with open(Dir+FILENAMESs[i],'rb') as imageFile:
                  Fzero = bytearray(imageFile.read())

        if(i==0):
            with open("DiffToOrig/"+str(i)+".bmp", "wb") as f:
                f.write(Fzero)
        else:
            with open(Dir+FILENAMESs[i-1],'rb') as imageFile:
                Fneg = bytearray(imageFile.read())
            Z=bytearray()
            for j in range(len(Fzero)):
                if(j<(14+7+16)):
                    Z.append(Fzero[j])
                else:
                    Z.append(Fneg[j]^Fzero[j])
            OldIm = Z
            with open("DiffToOrig/"+str(i)+".bmp", "wb") as f:
                f.write(OldIm)
    except Exception as e:
        print(e)

def SPEC(INN):
    return int(INN.split('.')[0])
def main():

    Dir = 'DiffOut/'
    Images=list()
    D=list()


    FILENAMES =  os.listdir(Dir)
    FILENAMES.sort(key=SPEC)

    if not os.path.exists('DiffToOrig'):
        os.makedirs('DiffToOrig')
    count=0
    for Fname in FILENAMES:
        with open(Dir+Fname,'rb') as imageFile:
            Fzero = bytearray(imageFile.read())
        if count==0:
            with open("DiffToOrig/"+str(count)+".bmp", "wb") as f:
                f.write(Fzero)
        else:
            Z=bytearray()
            for j in range(len(Fzero)):
                if(j<(14+7+16)):
                    Z.append(Fzero[j])
                else:
                    Z.append(FOld[j]^Fzero[j])
            with open("DiffToOrig/"+str(count)+".bmp", "wb") as f:
                f.write(Z)
            Fzero=Z
        count=count+1
        FOld=Fzero

if __name__ == '__main__':
    main()


    

