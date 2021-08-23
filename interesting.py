# cook your dish here
def GCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
t = int(input())
for i in range(t):
    k = int(input())
    add = 0
    for j in range(1, 2*k+1):
        a  = k+ j**2
        b = k + (j+1)**2
        add += GCD(a, b)
    
    print(add)