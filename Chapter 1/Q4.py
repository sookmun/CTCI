##need to try to implement this
def question4(input):
    alphabet=[0]*27
    # print(ord("a"))
    # print(ord(" "))
    for letter in input:
        letter=letter.lower()
        if letter ==" ":
            alphabet[0]+=1
        else:
            alphabet[ord(letter)-96]+=1
    # print(alphabet)
    odd=False
    for i in range (1,len(alphabet)):
        if alphabet[i] %2==0:
            continue
        elif odd ==False:
            odd=True
        else:
            return False
    return True


if __name__ == '__main__':
    print(question4("Tact Coa"))
    print(question4("redivider"))
    print(question4("mm add mamm"))