a=0
m=int(input("enter a value"))
n=int(input("enter a value"))
for i in range (m,n):
  print(i,end="")
  i=i+1
print("\n")
for i in range (m,n):
  if(i%2==0):
      print(i,end=" ")
print("\n")
for i in range (m,n):
  if(i%2!=0):
      print(i,end=" ")
      

