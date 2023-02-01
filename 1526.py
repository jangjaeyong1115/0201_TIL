N = int(input())

list1 = [{'7','4'},{'7'},{'4'}]

list2 = []

for i in range(N,-1,-1):
    list2.append(i)

for j in list2:
    if set(str(j)) in list1:
        print(j)
    break


# for i in range(int(input()),3,-1):
#    if not str(i).strip('47'):
#        print(i)
#        break