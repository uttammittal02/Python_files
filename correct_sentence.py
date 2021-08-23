def correct(s):
    for j in range(1,len(s)):
        k = list(s[j])
        if len(k) == 1:
            if k[0] in A or k[0] in B:
                continue
            else:
                print("NO")
                return
        elif k[0] in A:
            for l in range(1,len(k)):
                if k[l] not in A:
                    print("NO")
                    return
        elif k[0] in B:
            for l in range(1,len(k)):
                if k[l] not in B:
                    print("NO")
                    return
        else:
            print("NO")
            return
    print("YES")
    return
A = []
B = []
for a in range(97,110):
    A.append(chr(a))
for b in range(78,91):
    B.append(chr(b))
# print(A, B)
t = int(input())
for i in range(0,t):
    S = list(input().split())
    correct(S)