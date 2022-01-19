def counting_sort(list,b):
    """
    A counting sort that has an input lift of elements contain a tuple(digit,number). The counting sort will
    sort the tuple base on the digit. It will create an empty list and append it in countlist b times. b times
    because for example base 5 will not have a digit more than 5. Add the tuple base on the
    :param list: list of unsorted tuples
    :param b: the base of the list
    :return: a list sorted by a specific column
    :complexity: O(n + b) where b is the base because the countlist is size b and n is the input list
    """
    countlst=[0]*(b+1)
    for i in range(b+1):
        countlst[i] = []
    #sorting
    #adding the digit at list of index digit
    for i in list:
        countlst[i].append(i)
    index = 0
    #adding back the sorted list into the form [number.number...]
    for x in countlst: #at that digit
        for num in x: # making sure the sort is stable
            list[index]= num
            index+=1
    return list

if __name__ == '__main__':
    print(counting_sort([1,4,3,7,5,9,2,5,8],10))