def removeDups(Text):
    for i in len(Text):
        if i == i-1:
            print(i)
    return len(Text)
print(removeDups([1,0,1,0]))
print(removeDups(["The","big","cat"]))
print(removeDups(["John","Taylor","John"]))