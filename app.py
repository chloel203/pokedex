import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def pokedex(data):
    lang=input("what language? english, japanese, chinese, french? : ")
    for item in data:
        print(item["name"][lang])
    pokemon_type=input("what pokemon type do you want to view: ")
    pokemonfound=[]
    for item in data:
        if pokemon_type in item["type"]:
            pokemonfound.append(item["name"][lang])
            print(pokemonfound)
pokedex(data)
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

