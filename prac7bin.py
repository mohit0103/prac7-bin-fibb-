#BINARY SEARCH
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

key=int(input("enter no to search: "))

def binary_Search(p,key):
  L=0
  u=len(p)-1

  while L<=u:
    mid = (L+u)//2

    if p[mid] == key:
      return True
    else:
      if p[mid] < key:
        L=mid;
      else:
        u=mid;
      
if binary_Search(p,key):
  print("number found")
else:
  print("not found")
  
  
# FIBONACCI SEARCH
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

key=int(input("enter no to search: "))

def fibonacci_search(p, key):
    size = len((p))
     
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
     
    while(f2 > 1):
        i = min(start + f0, size - 1)
        if p[i] < key:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = i
        elif p[i] > key:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return i
    if (f1) and (p[size - 1] == key):
        return size - 1
    return -1

output = (fibonacci_search(p, key))

if output == -1:
  print("not found")
else:
  print('found')
