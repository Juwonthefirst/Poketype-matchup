from poke_dict import poke_dict
#import pandas as pd
#pokestats=pd.read_csv("/storage/emulated/0/modified_pokedata.csv")

a,b,c=True,True,True
#try putting the functions under the class to understand OOP better
#try a str to poketype converter
class poketype:
	def __init__(self,Asa, Awa,Ahne,Dsa, Dwa, Hne):
		self.Asa = Asa
		self.Awa = Awa
		self.Ahne = Ahne
		self.Dsa = Dsa
		self.Dwa = Dwa
		self.Hne = Hne
#pokemon types
Dark = poketype({"GHOST","PSYCHIC"},{"FIGHTING","BUG","FAIRY","DARK"},{" "},{"GHOST","DARK"},{"FIGHTING","BUG","FAIRY"},{"PSYCHIC"})
Psychic = poketype({"FIGHTING","POISON"},{"GHOST","PSYCHIC"},{"DARK"},{"POISON","FIGHTING","PSYCHIC"},{"STEEL","DARK","GHOST"},{" "})
Fire = poketype(
    {"GRASS", "ICE", "BUG", "STEEL"},
    {"FIRE", "WATER", "ROCK", "DRAGON"},
    {" "},
    {"FIRE", "ICE", "GRASS", "BUG", "STEEL", "FAIRY"},
    {"WATER", "GROUND", "ROCK"},
    {" "}
)

Water = poketype(
    {"FIRE", "GROUND", "ROCK"},
    {"WATER", "GRASS", "DRAGON"},
    {" "},
    {"FIRE", "WATER", "ICE", "STEEL"},
    {"ELECTRIC", "GRASS"},
    {" "}
)

Electric = poketype(
    {"WATER", "FLYING"},
    {"ELECTRIC", "GRASS", "DRAGON"},
    {"GROUND"},
    {"ELECTRIC", "FLYING", "STEEL"},
    {"GROUND"},
    {" "}
)

Ground = poketype(
    {"FIRE", "ELECTRIC", "POISON", "ROCK", "STEEL"},
    {"GRASS", "BUG"},
    {"FLYING"},
    {"POISON", "ROCK"},
    {"WATER", "GRASS", "ICE"},
    {"ELECTRIC"}
)

Rock = poketype(
    {"FIRE", "ICE", "FLYING", "BUG"},
    {"FIGHTING", "GROUND", "STEEL"},
    {" "},
    {"NORMAL", "FIRE", "POISON", "FLYING"},
    {"WATER", "GRASS", "FIGHTING", "GROUND", "STEEL"},
    {" "}
)

Dragon = poketype(
    {"DRAGON"},
    {"STEEL"},
    {"FAIRY"},
    {"ELECTRIC", "FIRE", "WATER", "GRASS"},
    {"ICE", "DRAGON", "FAIRY"},
    {" "}
)

Ice = poketype(
    {"GRASS", "GROUND", "FLYING", "DRAGON"},
    {"FIRE", "WATER", "ICE", "STEEL"},
    {" "},
    {"ICE"},
    {"FIRE", "FIGHTING", "ROCK", "STEEL"},
    {" "}
)

Fairy = poketype(
    {"FIGHTING", "DRAGON", "DARK"},
    {"FIRE", "POISON", "STEEL"},
    {" "},
    {"FIGHTING", "BUG", "DARK"},
    {"POISON", "STEEL"},
    {"DRAGON"}
)

Ghost = poketype(
    {"GHOST", "PSYCHIC"},
    {"DARK"},
    {"NORMAL"},
    {"BUG", "POISON"},
    {"GHOST", "DARK"},
    {"NORMAL", "FIGHTING"}
)

Fighting = poketype(
    {"NORMAL", "ICE", "ROCK", "DARK", "STEEL"},
    {"POISON", "FLYING", "PSYCHIC", "BUG", "FAIRY"},
    {"GHOST"},
    {"ROCK", "BUG", "DARK"},
    {"FLYING", "PSYCHIC", "FAIRY"},
    {" "}
)

Steel = poketype(
    {"ICE", "ROCK", "FAIRY"},
    {"FIRE", "WATER", "ELECTRIC", "STEEL"},
    {" "},
    {"NORMAL", "GRASS", "ICE", "FLYING", "PSYCHIC", "BUG", "ROCK", "DRAGON", "STEEL", "FAIRY"},
    {"FIRE", "FIGHTING", "GROUND"},
    {"POISON"}
)

Poison = poketype(
    {"GRASS", "FAIRY"},
    {"POISON", "GROUND", "ROCK", "GHOST"},
    {"STEEL"},
    {"GRASS", "FAIRY", "BUG", "FIGHTING", "POISON"},
    {"GROUND", "PSYCHIC"},
    {" "}
)

Bug = poketype(
    {"GRASS", "PSYCHIC", "DARK"},
    {"FIRE", "FIGHTING", "POISON", "FLYING", "GHOST", "STEEL", "FAIRY"},
    {" "},
    {"GRASS", "FIGHTING", "GROUND"},
    {"FIRE", "FLYING", "ROCK"},
    {" "}
)

Normal = poketype(
    {" "},
    {"ROCK", "STEEL"},
    {"GHOST"},
    {" "},
    {"FIGHTING"},
    {"GHOST"}
)

Grass = poketype(
    {"WATER", "GROUND", "ROCK"},
    {"FIRE", "GRASS", "POISON", "FLYING", "BUG", "DRAGON", "STEEL"},
    {" "},
    {"WATER", "ELECTRIC", "GRASS", "GROUND"},
    {"FIRE", "ICE", "POISON", "FLYING", "BUG"},
    {" "}
)

Flying = poketype(
    {"GRASS", "FIGHTING", "BUG"},
    {"ELECTRIC", "ROCK", "STEEL"},
    {" "},
    {"GRASS", "FIGHTING", "BUG"},
    {"ELECTRIC", "ICE", "ROCK"},
    {"GROUND"}
)
	
##############################
# dual type defense calculator
	
def DM(type1,type2):
	Hne = ((type1.Hne) | (type2.Hne))
	Dsa = (((type1.Dsa) - (type2.Dwa)) | ((type2.Dsa) - (type1.Dwa))) - Hne
	Dwa = (((type2.Dwa) - (type1.Dsa)) | ((type1.Dwa) - (type2.Dsa))) - Hne
	print("IN DEFENCE")
	print(Dsa, "is not very effective against this Pokemon")
	print(Dwa, "is very effective against this Pokemon")
	if " " in Hne:
		if type1.Hne != {" "}:
			print(type1.Hne, "has no effect against this pokemon")
		elif type2.Hne != {" "}:
			print(type2.Hne, "has no effect against this pokemon")
	else:
		print(Hne, "has no effect against this pokemon")
###########################		
############################
#dual type attack calculator block
def AM(type1,type2):
	Ahne = ((type1.Ahne) | (type2.Ahne))
	Asa = (type1.Asa) | (type2.Asa)
	Awa =(((type2.Awa) | (type1.Awa)) - Ahne) - Asa
	print("IN ATTACK")
	print("This pokemon is very effective against:", Asa)
	print("This pokemon is not very effective against",Awa)
	if " " in Ahne:
		if type1.Ahne != {" "}:
			print(f"The {inp} typing has no effect on",type1.Ahne)
		elif type2.Ahne != {" "}:
			print(f"The {inp2} typing has no effect on", type2.Ahne)
	else:
		print(f"The {inp} typing has no effect on {type1.Ahne}")
		print(f"The {inp2} typing has no effect on {type2.Ahne}")
#############################
#single type matchup block
def ST(type1):
	Asa = type1.Asa
	Awa = type1.Awa
	Ahne = type1.Ahne
	Dsa = type1.Dsa
	Dwa = type1.Dwa
	Hne = type1.Hne
	print("IN ATTACK")
	print("This pokemon is very effective against:",Asa)
	print("This pokemon is not very effective against",Awa)
	if Ahne != {" "}:
		print("This pokemon has no effect on", Ahne)
	print()
	print("IN DEFENCE")
	print(Dsa, "is not very effective against this Pokemon")
	print(Dwa,"is very effective against this Pokemon")
	if Hne != {" "}:
		print(Hne, "has no effect against this pokemon")
##############################
	
#X4 block	
def X4w(type1,type2):
	X4w = [I for I in type1.Dwa if I in type2.Dwa]
	if X4w != []:
		print(f"This Pokemon defense is X4 weak against {X4w}")
def X4s(type1,type2):
	X4s = [I for I in type1.Dsa if I in type2.Dsa] 
	if X4s != ([]):
		print(f"This Pokemon defense is X4 strong against {X4s}")
############################
		
#print type matchup
def print_type_matchup():
	print(f"The {inp} and {inp2} type pokemon")	
	AM(poke[inp],poke[inp2])
	print()
	DM(poke[inp], poke[inp2])
	X4s(poke[inp], poke[inp2])
	X4w(poke[inp],poke[inp2])
#############################
#dict search
def dict_search(poke_name):
	Ptype=poke_dict[poke_name]
	#if block to account for forme with type difference
	if type(Ptype)is dict:
		print(f"{poke_name} has {len(Ptype.keys())} forms\n Which Form do you want to check")
		for key in Ptype.keys():
			print(f"His {key} Forme")
		while True:
			try:
				form=input("Input a forme: ").strip(). capitalize()
				Ptype=poke_dict[poke_name][form]
				break
			except KeyError:
				print("invalid input, only Input the name of the forme, Do not add forme to the end")
		print(f"The {form} forme of:")
			
	if len(Ptype)==2:
		global inp
		inp=Ptype[0]
		global inp2
		inp2=Ptype[1]
		print(poke_name)
		print_type_matchup()
		print()
		more_info()
	else:
		inp=Ptype[0]
		print(f"{poke_name}, The {inp} type Pokemon")
		ST(poke[inp])
##############################
def more_info():
	while True:
		inp3 = input("Do you want to know more about each pokemon type: ").strip().lower()
		if inp3 == "yes":
			print()
			print(inp, "type")
			ST(poke[inp])
			print()
			print(inp2,"type")
			ST(poke[inp2])
			break
		elif inp3 == "no":
			print("GOTTA CATCH EM ALL")
			break
		else:
			print("invalid input, please pick  yes or no")
############################
#dict to convert str to class objects 
poke = {"Dark":Dark, "Psychic":Psychic, "Fire":Fire,"Water":Water,"Electric":Electric,"Ground": Ground,"Rock":Rock,"Dragon": Dragon,"Ice":Ice,"Fairy":Fairy,"Ghost":Ghost,"Fighting": Fighting,"Steel":Steel,"Poison": Poison,"Bug":Bug,"Normal": Normal,"Grass":Grass,"Flying": Flying}

# single type block
print("To search for Pokemon type matchup \n By type".ljust(45,"-"),"Input single or dual based on number of types")
print("By name".ljust(8,"-"),"input Pokemon name")
print()
while c:
	inp1 = input("input Single,Dual or Pokemon name: ").lower().strip()
	if inp1 == "single":
		try:
			inp = input("input the pokemon type: ").strip().capitalize()
			print(inp, "type")
			ST(poke[inp])
			c = False
		except KeyError:
			print("invalid pokemon type")

	
# dual type block
	elif inp1 == "dual":			
		while a:
			try:
				inp = input("input the first pokemon type: ").strip().capitalize()
				inp2 = input("input the second pokemon type: ").strip().capitalize()
				print_type_matchup()
				print()
				more_info()
				a,c=False,False					
			except KeyError:
				print("invalid pokemon type")
#search with Pokemon name				
	elif inp1.capitalize() in poke_dict.keys():
		pokeName= inp1.capitalize()
		dict_search(pokeName)
		c=False
	else:
		print("Invalid input, input Single, Dual or name of Pokemon")