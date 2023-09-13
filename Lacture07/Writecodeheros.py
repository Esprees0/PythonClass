Listname = []
Make_loop = 'y'
# def main():
#     Make_loop = str(input("Do you want to do again? (y/n)"))
#     while Make_loop.lower() == 'y':
        
def addhero(name):
    return Listname.append(name)

def insertheros(index,name):
    return Listname.insert(index,name)


def removeheros(name):
    return Listname.remove(name)

name_heros = ['Ironman','Thor','Hulk','Superman','Spiderman','Dr.Strange','Cpt. America','Black Panther', 'Ant Man']
print(name_heros,"or others heros you like")
print("What do you want to do" "\n1.Add heros" "\n2.Insert heros" "\n3.Renove heros")
Make_list = int(input("Select :"))

while Make_loop.lower() == 'y':
    if Make_list == 1:
        Select_heros = str(input("Hero you choose :"))
        addhero(Select_heros)
    elif Make_list == 2:
        insert_hero_index = int(input("Index you want: "))
        Select_heros = str(input("Hero you choose :"))
        insertheros(insert_hero_index,Select_heros)
    elif Make_list == 3:
        Remove_heros = str(input("Hero you want to renmove: "))
        removeheros(Remove_heros)
    print(Listname)
    Make_loop = str(input("Do you want to do again? (y/n)"))
print(Listname)

