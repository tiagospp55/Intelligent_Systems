def length(lista):
    if lista == []:
        return 0
    return 1 + length(lista[1:])

def sum(lista):
    if lista == []:
        return 0
    return lista[0] + sum(lista[1:])

def check_element(lista, element):
    if lista == []:
        return False
    if lista[0] == element:
            return True
    return check_element(lista[1:], element)

def concat(listaA, listaB):
     concat = listaA[0:]
     concat[-1:] = listaB
     return concat

def inverse(listaA):
     if listaA == []:
          return []
     return [listaA[-1]] + inverse(listaA[:-1])

def capicua(listaC):
    if listaC == []:
        return True
    if listaC[0] != listaC[-1]:
        return False

    print(listaC[1:-1])
    return capicua(listaC[1:-1])

def switch_xy(lista, x, y):
    if lista == []:
        return []
    if lista[0] == x:
        lista[0] = y
    return [lista[0]] + switch_xy(lista[1:], x,y )
    
    
     

listaA = [0, 1, 2, 3, 4, 5]
listaB = [6, 7, 8, 9]
listaC = [0, 1, 2, 3, 3, 2, 1, 0]
print('len ' + str(length(listaA)))
print('sum ' + str(sum(listaA)))
print('look 3 ' +str(check_element(listaA, 3)))
print('look 6 ' +str(check_element(listaA, 6)))
print('concat ', concat(listaA, listaB))
print('inverse ', inverse(listaA))
print('capicua True ', capicua(listaC))
print('capicua False ', capicua(listaA))
print('switch 2 by 0 ', switch_xy(listaC, 2,0 ))



