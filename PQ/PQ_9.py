lst = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            print(lst[i], lst[j], lst[k])
