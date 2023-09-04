import random

Rows = 3
Cols = 4 
def main():
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for r in range(Rows):
        for c in range(Cols):
            values[r][c] = random.randint(1,100)
        
    print(values)

main()