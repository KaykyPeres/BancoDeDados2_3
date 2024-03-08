from Pokedex import Pokedex
from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

Pokedex.getPokemonByName("Charizard")
Pokedex.getPokemonsByType(["Fire", "Fly"])
Pokedex.getFirePokemons()
Pokedex.getFireWeaknessPokemons()
Pokedex.getPokemonBySpawnChance()