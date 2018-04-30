n=int(input("enter the input:"))
c=0
while(n>0):
  m=n%10
  n=int(n/10)
  
  b=m**2
  c=c+b

print(c)
