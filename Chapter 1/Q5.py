
def oneAway(str1,str2):
    if len(str1)==len(str2):
        return checkReplace(str1,str2)
    elif len(str1)-len(str2)>=2 or len(str1)-len(str2)<=-2:
        return False
    elif len(str1)-len(str2):
        return checkInsert(str1,str2)

def checkInsert(str1,str2):
    pointer1=0
    pointer2=0
    flag=True
    if len(str2)>len(str1):
        str1,str2=str2,str1
    for index in range(len(str1)):
        if str1[pointer1]!=str2[pointer2] :
            if flag:
                pointer1+=1
                flag=False
            else:
                return False
    return True


def checkReplace(str1,str2):
    flag=True
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            if flag:
                flag=False
            else:
                return False
    return True


def checkRemove(str1,str2):
    pass

if __name__ == '__main__':
    # print(checkReplace("pale","bale"))
    # print(checkReplace("pale", "bake"))
    # print(oneAway("pale","palingkk"))
    print(oneAway("pale","ple"))
    print(oneAway("pales", "pale"))
    print(oneAway("pale", "bale"))
    print(oneAway("pale", "bake"))