def robot(row,column):
    map=[0]*row
    for r in range(row):
        map[r]=[0]*column
    map[0][0]="R"
    map[0][2]="X"
    position=(0,0)
    showMe(map)

    while position != (row-1,column-1):
        showMe(map)

        if position[1]+1<column and map[position[0]][position[1]+1] != "X":
            position=goRight(map,position)
        elif position[0]+1<row and map[position[0]+1][position[1]] != "X"   :
            position =goLeft(map,position)
        else:
            print("IM STUCK")
        print(position)
    showMe(map)

def showMe(lst):
    print(">>>"*10)
    for x in lst:
        print(x)
    print(">>>" * 10)

def goRight(lst,position):
    lst[position[0]][position[1]]=0
    lst[position[0]][position[1]+1] = "R"
    return (position[0],position[1]+1)

def goLeft(lst,position):
    lst[position[0]][position[1]]=0
    lst[position[0]+1][position[1]] = "R"
    return (position[0]+1,position[1])



if __name__ == '__main__':
    robot(3,5)