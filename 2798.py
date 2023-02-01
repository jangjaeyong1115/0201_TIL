import sys
a, b = map(int,sys.stdin.readline().split())

list = list(map(int,sys.stdin.readline().split()))

result = 0

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        for k in range(j+1,len(list)):
            sum = list[i] + list[j] + list[k]

            if sum <= b:
                result = max(result,sum)

    print(result)


