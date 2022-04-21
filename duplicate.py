list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
list3=[]

for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
print(list3)