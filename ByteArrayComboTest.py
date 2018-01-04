
#This makes frames for the difference, then blends them with the original frame
import timeit
import os, zlib,  io, concurrent.futures, subprocess
from operator import xor
import shutil




def CombOne(Fneg,Fzero):
            Z=bytearray(map(xor,Fzero,Fneg))
            for j in range(14+7+16):
                Z[j]=Fneg[j]
            OldIm = Z

def CombTwo(Fneg,Fzero):
            Z=bytearray(len(Fzero))
            for j in range(len(Fzero)):
                if(j<(14+7+16)):
                    Z[j]=(Fzero[j])
                else:
                    Z[j]=(Fneg[j]^Fzero[j])
            OldIm = Z
            


T1='JellyOut/out00001.bmp'
with open(T1,'rb') as imageFile:
    Fneg = bytearray(imageFile.read())
T2 = 'JellyOut/out00002.bmp'
with open(T2,'rb') as imageFile:
    Fzero = bytearray(imageFile.read())
            
def main():
    print("CombOne "+str(timeit.timeit("CombOne(Fneg,Fzero)",setup="from __main__ import CombOne,Fzero,Fneg",number=30)))
    print("CombTwo "+str(timeit.timeit("CombTwo(Fneg,Fzero)",setup="from __main__ import CombTwo,Fzero,Fneg",number=30)))

if __name__ == '__main__':
    main()


    

