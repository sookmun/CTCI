def stringCompression(string):
    retStr=""
    prev=""
    count=1
    lengthOfRet=0
    for index in range(len(string)):
        if lengthOfRet>len(string): # if can terminate early
            return string
        if index ==0:
            retStr+=string[index]
            lengthOfRet+=1
        elif prev ==string[index]:
            count+=1
        elif prev !=string[index]:
            retStr+=str(count)+string[index]
            lengthOfRet += 2
            count=1
        prev = string[index]

    retStr +=str(count)
    if len(retStr)>len(string):
        return string
    else:
        return retStr

if __name__ == '__main__':
    print(stringCompression("aabcccccaaa"))
    print(stringCompression("aa"))
    print(stringCompression("a"))
    print(stringCompression("abcdefghijk"))
    print(stringCompression("aAbcCcccaaA"))