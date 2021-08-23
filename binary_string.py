def list_to_number(lis):
    sum = 0
    n = len(lis)
    for i in range(n):
        sum += lis[i] * 2**(n-i-1)
    return sum
numbers = set()
def subsets(n, index, output, li):
    global numbers
    if index == n:
        if len(output) == 0:
            return
        else:
            #print(output)
            a = list_to_number(output)
            #print(a)
            numbers.add(a)
        return 
    subsets(n, index+1, output, li)
    output.append(li[index])
    subsets(n, index+1, output, li)
    output.pop()



for test_case in range(int(input())):
    numbers = set()
    binary_input = int(input())
    res = [int(x) for x in str(binary_input)]
    subsets(len(res), 0, [], res)
    num = list(numbers)
    num.sort()
    print(num)
    #found = False
    #if num[0] != 0:
    #    print(0)
    #    continue 
    #for i in range(len(num) - 1):
    #    if num[i+1] - num[i] != 1:
    #        a = num[i] + 1
    #        found = True
    #        break
    #if not found:
    #    a = num[len(num) - 1] + 1
    #a = str(bin(a))
    #for i in range(2, len(a)):
    #    print(a[i], end='')
    #print('')
#10#
#110101
#111101010
#1010101010101110
#11101010101011010
#1010101101011101011
#1111010101010101110
#1101010101011110101
#11110010101010101
#111101000000111010
#100000000000