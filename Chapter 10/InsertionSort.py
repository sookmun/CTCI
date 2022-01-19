def insertionSort(lst):
    for i in range(len(lst)):
        key=lst[i]

        j=i-1
        while j>=0 and key<lst[j]:
            lst[j+1]=lst[j]
            j-=1

        lst[j+1]=key
        print(lst)

if __name__ == '__main__':
    insertionSort([12, 11, 13, 5, 6])