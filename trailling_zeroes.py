

dic = {
    '1' : 'ab',
    '2' : 'b',
    '1' : 'c'
}
print(list(dict.items(dic)))

def trailing_zeroes(mid):
    count = 0
    while mid >= 5:
        print('while', mid, count)
        mid = mid//5
        count += mid
    return count

def required_number(q):
    if q == 0:
        return 1
    lo = 0
    hi = 10*q
    while lo<hi:
        mid = lo + (hi-lo)//2
        if trailing_zeroes(mid) == q:
            print('if', mid)
            return mid - mid%5
        elif trailing_zeroes(mid) > q:
            print('elif', mid)
            hi = mid-1
        else:
            print('else', mid)
            lo = mid + 1
    return 0


q = int(input())
if required_number(q) == 0:
    print('No solution')
else:
    print(required_number(q))
