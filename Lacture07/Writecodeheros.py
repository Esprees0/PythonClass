Listname = ['Ironman','Thor','Hulk','Superman','Spiderman','Dr.Strange','Cpt. America','Black Panther', 'Ant Man']
Make_loop = 'y'
def Show_hero(Listname):
    return Listname
def addhero(name):
    return Listname.append(name)

def insertheros(index,name):
    return Listname.insert(index,name)

def removeheros(name):
    return Listname.remove(name)

def Sortedlist_Ascend(Listname):
    return Listname.sort()

def Sortedlist_Descend(Listname):
    Listname.sort()
    return Listname.reverse()

print("What do you want to do" "\n1.Display hero" "\n2.Add heros" "\n3.Insert heros" "\n4.Renove heros" "\n5.Display Sorted Heros" "\n6.Exit")

while Make_loop.lower == 'y':
    Make_list = int(input("Select :"))
    if Make_list == 1:
        Show_hero(Listname)
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
            Sortedlist_Ascend(Listname)
        elif sorted_hero.upper == "D":
                Sortedlist_Descend(Listname)
        elif Make_list == 6:
            break
        print(Listname)
        Make_loop = str(input("Do you want to do again? (y/n):"))
            
print("The result",Listname)




