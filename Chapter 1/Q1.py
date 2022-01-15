def solution1():
    #in python hashtable can be in the form of the in built dictionary
    #if want a true/false whether string has duplicate return when key is found
    string="aasdkjcdfdookewdw"
    mydict={}
    for item in string:
        if mydict.get(item) is None:
            mydict.update({item: 1})
        else:
            mydict[item]+=1
    print(mydict)
    
