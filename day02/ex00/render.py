import sys, os

def func() :
    import re
    valuedic = {}
    if (sys.argv.__len__() != 2):
        print("Wrong number of arguments")
        return 1
    settings = open('settings.py')
    settingsStr = settings.read()

    exec(settingsStr, {}, valuedic)

    if(not sys.argv[1].endswith('.template')):
        print("Wrong file extension, should be .template")
        return 1
    if (not os.path.exists(sys.argv[1])):
        print("File path not found")
        return 1

    f = open(sys.argv[1])
    file = f.read()

    def check_and_replace(match) :
        value = valuedic.get(match.group(1))
        if(value) :
            return (value)
        else :
            return (match.group(0))

    string = re.sub("\\{(.*?)\\}", check_and_replace, file)
    with open("output.html", "w", encoding='utf-8') as file:
        file.write(string)
    return 0

if __name__ == '__main__' : 
    func()
