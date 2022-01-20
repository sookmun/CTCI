def smallestDifference(lstA,lstB):
    A=sorted(lstA)
    B=sorted(lstB)
    pointerA=0
    pointerB=0
    min=-1
    for index in range(len(lstB)-1):
        if min<0:
            min=abs(A[pointerA]-B[pointerB])
        else:
            check=abs(A[pointerA]-B[pointerB])
            if check < min :
                min=check

        if pointerA+1>=len(A):
            pointerB+=1
        elif pointerB+1>=len(B):
            pointerA+=1
        elif A[pointerA+1]>B[pointerB+1]:
            pointerB+=1
        else:
            pointerA+=1
        print("pA",pointerA)
        print("pB", pointerB)

    print(A[pointerA],B[pointerB])
    print("min",min)


if __name__ == '__main__':
    smallestDifference([1,3,15,11,2],[23,127,234,18,8])
    smallestDifference([1, 2, 15, 11], [4,235,23,12,127,19])