Listname = []

def addhero(name):
    Listname.add(name)
    return

def insertheros(index,name):
    Listname.insert(index,name)
    return

def removeheros(name):
    Listname.remove(name)
    return 

name_heros = ['Ironman','Thor','Hulk','Superman','Spiderman','Dr.Strange','Cpt. America','Black Panther', 'Ant Man']
print("Select the heros :",name_heros,"or others you wanna choose")

Select_heros = str(input("Hero you choose :"))
addhero(Select_heros)

insert_hero = ()
