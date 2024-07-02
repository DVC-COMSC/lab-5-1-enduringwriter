def getinput():
    v1 = int(input('Enter number: '))
    v2 = int(input('Enter number: '))
    return v1, v2

def getsum(v1, v2):
    total = v1 + v2
    return total

def printval(v1, v2, total):
    print(f'Total value: '{total})

def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
