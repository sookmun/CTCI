def sortStack(stack):
    tempStack=[]
    minimum=stack.pop()
    while len(stack)>0:
        if stack[-1] >minimum:
            tempStack.append(minimum)


if __name__ == '__main__':
    stack=[1,5,2,8,6,47]
    sortStack(stack)