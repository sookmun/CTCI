def bubbleSort(lst):
    length=len(lst)
    for i in range(length):
        print("outer")
        for j in range(0,length-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
            print(lst)
    return lst

if __name__ == '__main__':
    bubbleSort([64, 34, 25, 12, 22, 11,90])