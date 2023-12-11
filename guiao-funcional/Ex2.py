def separate(lista, side):
    if lista == []:
        return []

    if side == 'left':
        return [lista[0][0]] + separate(lista[1:], 'left')
    elif side == 'right':
        return [lista[0][1]] + separate(lista[1:], 'right')  
    
def remove_and_count(list,x,cnt = 0):
    if list == []:
        return []
    if list[0] == x:
        return remove_and_count(list[1:],x, cnt+1)
    return ([list[0]] + remove_and_count(list[1:], x, cnt)), cnt


def count_elements(list):
    pass
    
list1 = [(1,2), (3,4), (5,6), (7,8)]
print('separate', (separate(list1,'left'),separate(list1, 'right')))
list2 = [1 ,2 ,3, 4, 5, 6, 1, 1,1 ,1]
print('remove_and_count', remove_and_count(list2,1))