for _ in range(int(input())):
    arr=[0]*3
    arr[0]= input()
    arr[1]= input()
    arr[2]= input()
    X_=0
    O_=0
    __=0
    row_wise=0
    
    X_count=0
    O_count=0
    for i in range(3):
        word= arr[i]
        for i in range(3):
            if word[i]=="X":
                X_+=1
                X_count+=1
            elif word[i]=="O":
                O_+=1
                O_count+=1
            elif word[i]=="_":
                __+=1
        if X_count==3 or O_count==3:
            row_wise+=1
        # print("X_count = ", X_count, "O_count = ", O_count)
        X_count=0
        O_count=0
    

    if abs(X_ - O_)>1 or (row_wise>=2 ):
        print("3")
        continue
 
    for i in range(3):
        if arr[0][i]=="X":
            X_count+=1
        if arr[0][i]=="O":
            O_count+=1
        if arr[1][i]=="X":
            X_count+=1
        if arr[1][i]=="O":
            O_count+=1
        if arr[2][i]=="X":
            X_count+=1
        if arr[2][i]=="O":
            O_count+=1
        if X_count==3 or O_count==3:
            row_wise+=1
        X_count=0
        O_count=0
    if (row_wise>=2 ):
        print("3")
        continue
    #for i in range(1):
    if arr[0][0]=="X":
        X_count+=1
    if arr[0][0]=="O":
        O_count+=1
    if arr[1][1]=="X":
        X_count+=1
    if arr[1][1]=="O":
        O_count+=1
    if arr[2][2]=="X":
        X_count+=1
    if arr[2][2]=="O":
        O_count+=1
    if X_count==3 or O_count==3:
        row_wise+=1
    X_count=0
    O_count=0
    #for i in range(1):
    if arr[0][2]=="X":
        X_count+=1
    if arr[0][2]=="O":
        O_count+=1
    if arr[1][1]=="X":
        X_count+=1
    if arr[1][1]=="O":
        O_count+=1
    if arr[2][0]=="X":
        X_count+=1
    if arr[2][0]=="O":
        O_count+=1
    if X_count==3 or O_count==3:
        row_wise+=1
    X_count=0
    O_count=0
    # print("row_wise = ", row_wise)
    if (row_wise>=2):
        print("3")
        continue
    if row_wise==1:
        print("1")
        continue
    if __==0:
        print("1")
        continue
    if __>0:
        print("2")
        
    
        

    
        
        






