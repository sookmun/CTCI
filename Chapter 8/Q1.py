def tripleStep(counter):
    if counter==0:
        return 1
    elif counter<0:
        return 0
    else:
        return tripleStep(counter-1)+tripleStep(counter-2)+tripleStep(counter-3)


if __name__ == '__main__':
    print(tripleStep(4))