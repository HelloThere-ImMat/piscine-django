
def func() :
    import re
    valuedic = {}

    settings = open("settings.py")
    settingsStr = settings.read()

    exec(settingsStr, {}, valuedic)
    f = open("file.template")
    file = f.read()

    def check_and_replace(match) :
        value = valuedic.get(match.group(1))
        if(value) :
            return (value)
        else :
            return (match.group(0))

    string = re.sub("\{(.*?)\}", check_and_replace, file)
    print(string)

if __name__ == '__main__' : 
    func()