import math
import os
import random
import re
import sys

def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s

def flipping(matrix, nLen, bCol, nCnt): # 뒤집기 사용안함
    if bCol == True:
        for i in range(int(nLen/2)):
            nTemp = matrix[i][nCnt]
            matrix[i][nCnt] = matrix[nLen-i-1][nCnt]
            matrix[nLen-i-1][nCnt] = nTemp
  
    else:
        for i in range(int(nLen/2)):
            nTemp = matrix[nCnt][i]
            matrix[nCnt][i] = matrix[nCnt][nLen-i-1]
            matrix[nCnt][nLen-i-1] = nTemp                  
    
    return matrix

def flippingMatrix2(matrix):  #사용안함
    nLen = len(matrix)    

    while(True):        
        bClearC = True
        bClearR = True
        lMax = [0,0]        
       
        for i in range(nLen):            
            nSum = 0
            for j in range(nLen):                
                if j < nLen/2:
                    nSum += matrix[j][i]                    
                else:
                    nSum -= matrix[j][i] 
            if nSum < lMax[0]:
                lMax[0] = nSum
                lMax[1] = i
                bClearC = False
        
        if bClearC == False:
            flipping(matrix, nLen, True, lMax[1])

        lMax = [0,0]
        for i in range(nLen):   
            nSum = 0        
            for j in range(nLen):
                if j < nLen/2:
                    nSum += matrix[i][j]                    
                else:
                    nSum -= matrix[i][j] 
            if nSum < lMax[0]:
                lMax[0] = nSum
                lMax[1] = i
                bClearR = False                

        if bClearR == False:
            flipping(matrix, nLen, False, lMax[1])                

        if (bClearC and bClearR):
            nSumVal = 0
            for i in range(int(nLen/2)): 
                for j in range(int(nLen/2)):
                    nSumVal += matrix[i][j]
            return nSumVal



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
