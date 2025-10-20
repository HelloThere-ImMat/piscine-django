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
    if (sys.argv[1] in capital_cities.values()) :
        stateCode = next((k for k, v in capital_cities.items() if v == sys.argv[1]), None)
        state = next((k for k, v in states.items() if v == stateCode), None)
        print(state)
    else : 
        print("Unknown capital city")
    return (0)

        


if __name__ == '__main__' :
    funct()