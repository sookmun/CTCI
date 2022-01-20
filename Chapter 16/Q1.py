def numberSwapper():
    a=9
    b=14
    if a>b:
        print("a:",a,"b:",b)
        a=a-b
        b=a+b
        a=b-a
        print("a:", a, "b:", b)
    else:
        b=b-a
        a=a+b
        b=a-b
        print("a:", a, "b:", b)
    print()

if __name__ == '__main__':
    numberSwapper()