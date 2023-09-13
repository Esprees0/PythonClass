Listname = []
Make_loop = 'y'

def addhero(name):
    return Listname.append(name)

def insertheros(index,name):
    return Listname.insert(index,name)

def removeheros(name):
    return Listname.remove(name)

name_heros = ['Ironman','Thor','Hulk','Superman','Spiderman','Dr.Strange','Cpt. America','Black Panther', 'Ant Man']
print(name_heros)
print("What do you want to do" "\n1.Display hero" "\n2.Add heros" "\n3.Insert heros" "\n4.Renove heros" "\n5.Display Sorted Heros")


while Make_loop.lower() == 'y':
    Make_list = int(input("Select :"))
    if Make_list == 1:
        Listname = [] + name_heros
    elif Make_list == 2:
        Select_heros = str(input("Hero you choose :"))
        addhero(Select_heros)
    elif Make_list == 3:
        insert_hero_index = int(input("Index you want: "))
        Select_heros = str(input("Hero you choose :"))
        insertheros(insert_hero_index,Select_heros)
    elif Make_list == 4:
        Remove_heros = str(input("Hero you want to renmove: "))
        removeheros(Remove_heros)
    elif Make_list == 5:
        sorted_hero = str(input("Ascending/Descending (A/D):"))
        if sorted_hero.upper == "A":
            Listname.sort()
        elif sorted_hero.upper == "D":
            Listname.sort()
            Listname.reverse()
            
    elif Make_list == 6:
        break
    print(Listname)
    Make_loop = str(input("Do you want to do again? (y/n):"))
        
print(Listname)

