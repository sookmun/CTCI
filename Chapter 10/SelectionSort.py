def selectionSort(lst):
    for i in range(len(lst)):
        minimum=i
        print("outer")
        print(lst)
        for j in range(i+1,len(lst)):

            if lst[minimum]>lst[j]:
                minimum=j
        lst[i],lst[minimum]=lst[minimum],lst[i]
        print("inner")
        print(lst)
    return lst

if __name__ == '__main__':
    selectionSort([64, 25, 12, 22, 11])