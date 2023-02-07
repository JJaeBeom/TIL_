###정렬안된 검색

#정렬된 검색
list_a = [1, 2, 3, 4, 5, 6, 7, 8]

def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key :
        return i
    else:
        return -1
    
print(sequentialSearch2(list_a, 8, 5))
###########
