def numbersPrint() :
    file = open("numbers.txt")
    str = file.read()
    list = str.split(',')
    for x in list :
        print(x)

if __name__ == '__main__':
    numbersPrint()