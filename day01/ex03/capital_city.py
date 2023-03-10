import sys

def listCapitals(input_user):
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

    if not(input_user in states):
        sys.exit("Unknown state")
    print(capital_cities[states[input_user]])






if __name__ == '__main__':
    if(len(sys.argv) != 2):
        sys.exit()
    listCapitals(sys.argv[1])