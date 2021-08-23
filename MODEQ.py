from sys import stdin, stdout

def factor_pairs(limit) :
    total = 0
    for a in range(1,((limit+1)//2) +1) :
        total += (limit//a) - 1
    return total

def non_factor_pairs(n,m) :
    total = 0
    def required_divisors(num,b) :
        a,divisors = 1,0
        while a*a <= num :
            if num%a == 0  :
                if b > a and b%a != 0 :divisors += 1
                x = num//a
                if b > x and x!= a and b%x != 0 :divisors += 1
            a += 1
        return divisors

    x = min(n,(m+1)//2)
    for b in range(2,x + 1) :
        num = m//b
        total += required_divisors(num,b)

    if n > m :
        total += (n-m)*(m+n-1)//2
    return total

for test in range(int(stdin.readline().rstrip())) :
    n,m =  map(int, stdin.readline().rstrip().split())
    pairs = factor_pairs(min(m,n)) + non_factor_pairs(n,m)
    stdout.write(f'{pairs}' + '\n')