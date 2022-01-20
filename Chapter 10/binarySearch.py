def binarySeach_Iter(lst,item):
    low=0
    high=len(lst)

    while low<=high:
        print("high:",high)
        print("low:",low)

        mid=(high+low)//2
        print("mid:", mid)
        if lst[mid]==item:
            return mid
        elif lst[mid]<item:
            low=mid+1
        elif lst[mid]>item:
            high=mid- 1
    return "not in list"

def binarySearch_Recursive(lst,item,low,high):
    print("low:",low)
    print("high:",high)
    if high>=low:
        mid=(high+low)//2
        if lst[mid]== item:
            return mid
        elif lst[mid]>item:
            return binarySearch_Recursive(lst,item,low,mid-1)
        else:
            return binarySearch_Recursive(lst,item,mid+1,high)
    else:
        return "item not in list"

if __name__ == '__main__':
    binarySeach_Iter([ 2, 3, 4, 10, 40 ],40)
    # print(binarySearch_Recursive([ 2, 3, 4, 10, 40 ],40,0,5))

