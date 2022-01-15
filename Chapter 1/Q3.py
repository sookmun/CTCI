def method1(string,length):
    lst=[""]*length
    retstring=""
    index=0
    for letter in string:
        if letter==" ":
            lst[index]="%20"
        else:
            lst[index] = letter
        index+=1
        if index>=length:
            break
    for item in lst:
        retstring+=item
    print(retstring)


if __name__ == '__main__':
    method1("Mr John Smith    ", 13)