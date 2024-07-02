def getinput():
    userval1 = input('Enter value: ')
    return userval1

def getsum(v1, v2):
    userval1 = int(input('Enter number: '))
    userval2 = int(input('Enter number: '))

def printval(v1, v2, total):
    # ******************************
    # Make your Code
    # ******************************


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
