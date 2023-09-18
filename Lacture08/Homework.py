def maxProductExplanation(n):
    Multiply = split_Product(n)
    String_split = ' + '.join(map(str,Multiply))
    String_Multi = ' × '.join(map(str,Multiply))
    Find_MultiplyProduct(Multiply)
    Result = (f'Input: n = {n}\nOutput: {Find_MultiplyProduct(Multiply)}\nExplanation: {n} = {String_split}, {String_Multi} = {Find_MultiplyProduct(Multiply)}')
    return Result

def split_Product(Product):
    Split_product = []
    if Product == 0 or Product == 1:
        Split_product.append(Product)
    elif Product <= 5:
        Split_product.append(Product//2)
        Split_product.append(Product//2 + Product%2)
    elif Product > 4:
        Num = 0
        for i in range(Product,0,-1):
            Num += 1
            if Num == 3:
                Split_product.append(3)
                Num = 0
            elif i == 4:
                Split_product.append(2)
                Split_product.append(2)
                break
    Split_product.sort()
    return Split_product

def Find_MultiplyProduct(Product):
    Mulitply_list = 1 
    for k in Product:
        Mulitply_list *= k
    return Mulitply_list


# Example usage
print(maxProductExplanation(2))
print(maxProductExplanation(5))
print(maxProductExplanation(7))
print(maxProductExplanation(10))
print(maxProductExplanation(15))

