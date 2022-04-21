marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
for i in marks:
    max=0
    for j in i:
        # print(j)
        if j>max:
            max=j
    print(max)
