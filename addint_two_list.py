list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list3=[]
for i in list1:
    if i not in list3:
        list3.append(i)
for i in list2:
    if i not in list3:
        list3.append(i)
list3.sort()

print(list3)