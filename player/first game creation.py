while (1):
 import random
 arr=['p','s','sc']
 c=random.choice(arr)
 v=str(input("enter the your choice form -- s, sc,  p:"))
 b=str(v)
 n=str(c)
 print(b)
 print(n)
 if(c==v):
   print("match draw")
 elif(b=="s" and n=="sc"):
   print("vijay is win")
 elif(b=="s" and n=="p"):
   print("computer is win")
 elif(b=="p" and n=="s"):
   print("vijay is win")
 elif(b=="p" and n=="sc"):
   print("computer is win")  
 elif(b=="sc" and n=="p"):
   print("vijay is win")
 elif(b=="sc" and n=="s"):
   print("computer is win")
