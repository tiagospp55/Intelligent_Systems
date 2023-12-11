#Exercicio 1.1
def comprimento(lista):
	if lista == []:
		return []
	else:
		return 1 + comprimento(lista[1:])


#Exercicio 1.2
def soma(lista):
	if lista == []:
		return []
	else:
		return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if lista == []:
		return []
	else:
		if lista == elem:
			return True
	return existe(lista[1:], elem)
	pass

#Exercicio 1.4
def concat(l1, l2):
	if l1 == [] or l2 == []:
		return []
	else:
		return l1 + l2

#Exercicio 1.5
def inverte(lista):
	if lista == []:
		return []
	else:
		return lista[-1] + inverte(lista[:-1])

#Exercicio 1.6
def capicua(lista):

	pass

#Exercicio 1.7
def concat_listas(lista):
	pass

#Exercicio 1.8
def substitui(lista, original, novo):
	if lista == []:
		return []
	else:
		if lista == [original]:
			return [novo] + substitui(lista[1:], original, novo)
		else:
			return lista[0] + substitui(lista[1:], original, novo)
	pass

#Exercicio 1.9
def fusao_ordenada(lista1, lista2):
	if lista1 == [] or lista2 == []:
		return []
	else:
		if lista1[0] < lista2[0]:
			return lista1[0] + fusao_ordenada(lista1[1:], lista2)
		else:
			return lista2[0] + fusao_ordenada(lista1, lista2[1:])

#Exercicio 1.10
def lista_subconjuntos(lista):
		# Quê?
	pass


#Exercicio 2.1
def separar(lista):
	 #Está mal
	if lista == []:
		return []
	else:
		primeiroElemento, segundoElemento = lista[0]
		return ([primeiroElemento], [segundoElemento]) + separar(lista[1:])
	pass

#Exercicio 2.2
def remove_e_conta(lista, elem):

	if lista == []:
		return []
	elif lista == elem:
			return [(remove_e_conta(lista[1:], elem), 1)]

	return lista [0] + remove_e_conta(lista[1:], elem)		

	pass

#Exercicio 3.1
def cabeca(lista):
	if lista == []:
		return None
	return lista[0]
	pass

#Exercicio 3.2
def cauda(lista):
	if lista == []:
		return None
	return lista[1:]
	pass



#Exercicio 3.4
def menor(lista):
	if lista == []:
		return None
	if len(lista) == 1:
		return lista[0]

	return min(lista[0], menor(lista[1:]))
	pass

#Exercicio 3.6
def max_min(lista):
	if lista == []:
		return None
	if len(lista) == 1:
		return (lista[0],[])
	
	(m,l) = menor(lista[1:])

	if lista[0] < m:
		return (lista[0],l)
	return (m, [lista[0]] + l) 
	
	pass




lista = [(1,1), (2,2), (3,3), (4,4)]
print(separar(lista))