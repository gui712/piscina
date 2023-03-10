import sys
def listCities(input_user):
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

    if not(input_user in capital_cities.values()):
        sys.exit("Unknown capital city")

    for key, value in capital_cities.items():
        if(input_user == value):
            new_value = key

    for key, value in states.items():
        if(new_value == value):
            print(key)


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        sys.exit()
    listCities(sys.argv[1])