import sys

def funct() :
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if (sys.argv.__len__() != 2) :
        return (1)
    split = sys.argv[1].split(',')
    for e in split :
        if (e in capital_cities.values()) :
            stateCode = next((k for k, v in capital_cities.items() if v == e), None)
            state = next((k for k, v in states.items() if v == stateCode), None)
            print(e, "is the capital of", state)
        elif (e in states.keys()) :
            print(e, "is a state")
        else :
            print(e, "is neither a capital city nor a state")         
    return (0)

if __name__ == '__main__':
    funct()