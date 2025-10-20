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
    if (sys.argv[1] in states) :
        print(capital_cities[states[sys.argv[1]]])
    else :
        print("Unknown state")
    return (0)  

        


if __name__ == '__main__' :
    funct()