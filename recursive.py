

def printNumbers(a):
   
    if(a<10):
        a=a+1
        printNumbers(a)
    print(a)      
   

printNumbers(1)

