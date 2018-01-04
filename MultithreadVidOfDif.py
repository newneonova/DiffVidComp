import os, zlib,  io, concurrent.futures

def MakeDiff(i,FILENAMESs,Dir):
    print(str(i))
    try:
        with open(Dir+FILENAMESs[i],'rb') as imageFile:
                  Fzero = bytearray(imageFile.read())

        if(i==0):
            with open("DiffOut/"+str(i)+".bmp", "wb") as f:
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
            with open("DiffOut/"+str(i)+".bmp", "wb") as f:
                f.write(OldIm)
    except Exception as e:
        print(e)

def main():

    Dir = 'JellyOut/'
    Images=list()
    D=list()


    FILENAMES =  os.listdir(Dir)

    if not os.path.exists('DiffOut'):
        os.makedirs('DiffOut')

    executor = concurrent.futures.ProcessPoolExecutor(8)
    futures = [executor.submit(MakeDiff, i, FILENAMES,Dir) for i in range(len(FILENAMES))]
    concurrent.futures.wait(futures)

if __name__ == '__main__':
    main()


    

