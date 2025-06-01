
def patfunc():
    x,y=map(int,input("Enter the rows and columns").split())
    tt=int(input(("Enter 1 for upward triangle(asterisk), 2 for downward triangle(asterisk),3 for centered triangle(asterisk), 4 for triangle of numbers ")))

    if tt==1:
        for i in range(1,x+1):
            for j in range(i):
                print("*",end='')
            print()
    elif tt==2:
        for i in range(x,0,-1):
            for j in range(i):
                print("*",end=' ')
            print()
    elif tt==3:
        for i in range(x):
            for j in range(x-i):
                print(" ",end='')
            for k in range((2*i-1)):
                if k%2!=0:
                    print(" ",end='')
                else:
                    print("*",end='')
            print()
    else:
        k=1
        for i in range(1,x+1):
            for j in range(i):
                print(k,end=' ')
                k+=1
            print()

patfunc()

