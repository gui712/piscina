import sys

def valid_capital(input_user,states, capital_cities):
    for key, value in capital_cities.items():
        if(input_user == value):
            new_value = key
    for key, value in states.items():
        if(new_value == value):
            print(f'{input_user} is the capital of {key}')        


def statesOrCities(input_user): 
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

    text = input_user.split(',')

    for i in text:
        inp = i.strip(' ').title()
        if(inp != ''):
            if(inp in states):
                print(f'{capital_cities[states[inp]]} is the capital of {inp}')
            elif(inp in capital_cities.values()):
                valid_capital(inp, states, capital_cities)
            else:
                print(f'{inp} is neither a city nor a state')        



if __name__ == '__main__':
    if(len(sys.argv) != 2):
        sys.exit()
    statesOrCities(sys.argv[1])