# def list_to_number(lis):
#     sum = 0
#     n = len(lis)
#     for i in range(n):
#         sum += lis[i] * 2**(n-i-1)
#     return sum

def if_subsequence_present(binary_no, target):
    m= len(binary_no)
    n= len(target)
    i=0
    if n==m:
        if binary_no==target:
            return True
        else:
            return False
    checker=0
    for x in range(m):
        if binary_no[x] == target[i]:
            i+=1
        if i==n:
            return True
    return False

def generatePrintBinary(n):
     
    
    from queue import Queue
    q = Queue()
    
    for i in range(97, 123):
        q.put(chr(i))
        
    while(n > 0):
        n -= 1
        s1 = q.get()
        arr.append(s1)
        for i in range(97, 123):
            s2 = s1
            q.put(s2+chr(i))

n=4
arr=[]
# list_to_number([1, 0, 1, 0, 0, 1])
arr.append("a")
generatePrintBinary(n)
for _ in range(int(input())):
    word=input()
    for __ in range(len(arr)):
        if not if_subsequence_present(word, arr[__]):
            print(arr[__])
            break