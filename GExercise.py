
def strWithout3a3b(a: int, b: int) -> str:
    res = ""

    while a or b:
        if res[-2:] == "aa":
            print("in first")
            # print("res", res)
            # print("zzz", res[-2:])
            res += "b"
            b -= 1
        elif res[-2:] == "bb":
            print("in second")
            res += "a"
            a -= 1
        elif a > b:
            print("in third")
            res += "a"
            a -= 1
        else:
            print("in fourth")
            res += "b"
            b -= 1
        print(">"*20)
        print("a:",a)
        print("b:", b)
        print("res",res)
        print(">" * 20)

    return res


def chips(numOfChips,numAllIn):

    rounds=0
    hisChip=1
    while hisChip<numOfChips:
        if hisChip==1:
            hisChip+=1
        elif numAllIn>0:
            hisChip*=2
            numAllIn-=1
        else:
            hisChip+=1
        rounds+=1
    print("hiss:",hisChip)
    return rounds






if __name__ == '__main__':
    # strWithout3a3b(5,2)
    # print(chips(234, 23))
    print(solution(234, 23))