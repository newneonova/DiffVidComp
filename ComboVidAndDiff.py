
#This makes frames for the difference, then blends them with the original frame

import os, zlib,  io, concurrent.futures, subprocess
from PIL import Image
from PIL import ImageDraw
from operator import xor
import shutil

def MakeDiff(i,FILENAMESs,DIRNAMEIN,DIRNAMEOUT):
    print(str(i))
    try:
        with open(DIRNAMEIN+"/"+FILENAMESs[i],'rb') as imageFile:
                  Fzero = bytearray(imageFile.read())

        if(i==0):
            with open(DIRNAMEOUT+"/"+str(i)+".bmp", "wb") as f:
                f.write(Fzero)
        else:
            with open(DIRNAMEIN+"/"+FILENAMESs[i-1],'rb') as imageFile:
                Fneg = bytearray(imageFile.read())
       
            Z=bytearray(map(xor,Fneg,Fzero))
            for j in range(14+7+16):
                Z[j]=Fzero[j]
            OldIm = Z
            with open(DIRNAMEOUT+"/"+str(i)+".bmp", "wb") as f:
                f.write(OldIm)
            imOne = Image.open(DIRNAMEOUT+"/"+str(i)+".bmp")
            imTwo = Image.open(DIRNAMEIN+"/"+FILENAMESs[i])
            newImage = Image.blend(imOne,imTwo,.8)
            newImage.save(DIRNAMEOUT+"/"+str(i)+".bmp")

            

    except Exception as e:
        print(e)
def SPEC(INN):
    return int(INN.split('.')[0])

def main():
    InVid = input("Filename: ")
    DIRNAMEIN = InVid.split('.')[0]
    DIRNAMEOUT = DIRNAMEIN+'_DIFF'
    if not os.path.exists(DIRNAMEIN):
        os.makedirs(DIRNAMEIN)
    if not os.path.exists(DIRNAMEOUT):
        os.makedirs(DIRNAMEOUT)
    print("Calling ffmpeg to split video into image files...")
    subprocess.call(
        'ffmpeg -i '+InVid+' '+DIRNAMEIN+'/%d.bmp',
    shell=True)
    FILENAMES =  os.listdir(DIRNAMEIN)
    FILENAMES.sort(key=SPEC)
    print("Creating diff frames...")
    executor = concurrent.futures.ProcessPoolExecutor(8)
    futures = [executor.submit(MakeDiff, i, FILENAMES,DIRNAMEIN,DIRNAMEOUT) for i in range(len(FILENAMES))]
    concurrent.futures.wait(futures)
    print("Creating .mp4...")
    subprocess.call(
        'ffmpeg -i '+DIRNAMEOUT+'/%d.bmp'+' DIFF_'+InVid,
    shell=True)
    
    shutil.rmtree(DIRNAMEIN)
    shutil.rmtree(DIRNAMEOUT)
  

if __name__ == '__main__':
    main()


    

