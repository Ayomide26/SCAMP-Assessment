#fibonacci number is a number thatrstarts from 0 to 1
#fibonacci sequence are 0,1,1,2,3,5,8,13,21,34...
#0+1=1
#1+1=2
#1+2=3
#2+3=5
#3+5=8...
n=int(input("Enter a number:"))
if n==0:
      fib=[0]
elif n==1:
       fib=[1]
elif n==2:
    fib=[1,1]
else:
    fib=[1,1]
    for i in range(1,n):
        fib.append(fib[i-0]+fib[i-1])
print(fib)
