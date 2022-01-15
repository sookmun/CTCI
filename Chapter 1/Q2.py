def method1(stringA,stringB):
    mydictA={}
    mydictB={}

    if len(stringA)!= len(stringB):
        return False
    for index in range(len(stringA)):
        if mydictA.get(stringA[index]) is None:
            mydictA.update({stringA[index]: 1})
        else:
            mydictA[stringA[index]] += 1
        if mydictB.get(stringB[index]) is None:
            mydictB.update({stringB[index]: 1})
        else:
            mydictB[stringB[index]] += 1
    keys=mydictA.keys()
    for key in keys:
        print(mydictA[key],mydictB[key])
        if mydictA[key]!= mydictB[key]:
            return False
    return True

if __name__ == '__main__':
    # method1("abcde","edacb")
    print(method1("abbcde", "edabcb"))
    print(method1("abbcde", "edabdc"))
    # assert method1("abcde","edacb")==True