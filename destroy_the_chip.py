import sys
lx, rx, ly, ry  = 0,0,0,0

def HellofFire(midx, midy):
    global lx, rx, ly, ry, cnt
    cnt += 1
    answer = input()
    if answer == "O":
        return "success"
    elif answer == "PY":
        rx = midx-1
        return "Y"
    elif answer == "NY":
        lx = midx+1
        return 'Y'
    elif answer == "XP":
        ry = midy-1
        return 'X'
    elif answer == "XN":
        ly = midy+1
        return 'X'
    elif answer == "PP":
        rx = midx - 1
        ry = midy - 1
    elif answer == "PN":
        rx = midx - 1
        ly = midy + 1
    elif answer == "NP":
        lx = midx + 1
        ry = midy - 1
    elif answer == "NN":
        lx = midx + 1
        ly = midy + 1
    else:
        cnt-=1
        if answer == "FAILED":
            #print("failed either due to excess queries or invalid attack statement")
            exit(0)

def RingofFire(lx, rx, ly, ry):
    global cnt
    cnt+=1
    print(2, lx, ly, rx, ry)
    answer = input()
    if answer == 'IN':
        return RingofFire(lx, rx, ly, ry)
    elif answer == 'O':
        return 'success'



def BinarySearch():
    global cnt, q, lx, rx, ly, ry
    #lx, rx, ly, ry = -62, -60, -1, 8
    lx, rx, ly, ry = int(-2e18), int(2e18), int(-2e18), int(2e18)
    while lx<=rx or ly<=ry:
        midx = (lx+rx)//2
        midy = (ly+ry)//2
        
        print(1, midx, midy, flush=True)
        sys.stdout.flush()
        output1 = HellofFire(midx, midy)
        if output1 == 'success':
            return
        lx-=1
        rx+=1
        ly-=1
        ry+=1
        #print(f'lx = %d, rx = %d, ly = %d, ry = %d' %(lx, rx, ly, ry))
        if rx-lx == 2 and ry-ly == 2:
            output2 = RingofFire(lx, rx, ly, ry)
            if output2 == 'success':
                return
        elif rx - lx == 2 and output1 == "Y":
            output2 = RingofFire(lx, rx, midy - 1, midy + 1)
            if output2 == 'success':
                return
        elif ry - ly == 2 and output1 == "X":
            output2 = RingofFire(midx - 1, midx + 1, ly, ry)
            if output2 == 'success':
                return
        if cnt > q:
            print('FAIL')
            exit(0)
      
#brackets(5)   
t, q, d = map(int, input().split())
for i in range(t):
    cnt = 0
    if d == 0:
        lx, rx, ly, ry = int(-2e18), int(2e18), int(-2e18), int(2e18)
        while lx<=rx or ly<=ry:
            cnt += 1
            midx = (lx+rx)//2
            midy = (ly+ry)//2
            print(1, midx, midy, flush=True)
            sys.stdout.flush()
            answer = input()
            if answer == "O":
                break
            elif answer == "PY":
                rx = midx-1
            elif answer == "NY":
                lx = midx+1
            elif answer == "XP":
                ry = midy-1
            elif answer == "XN":
                ly = midy+1
            elif answer == "PP":
                rx = midx - 1
                ry = midy - 1
            elif answer == "PN":
                rx = midx - 1
                ly = midy + 1
            elif answer == "NP":
                lx = midx + 1
                ry = midy - 1
            elif answer == "NN":
                lx = midx + 1
                ly = midy + 1

            if answer == "FAILED" or cnt > q:
                #print("failed either due to excess queries or invalid attack statement")
                exit(0)
        continue
    BinarySearch()

