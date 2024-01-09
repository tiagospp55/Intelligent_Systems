



# Redes semanticas
# -- Exemplo
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2019
# 2019/10/20
#


from semantic_network import *

a = Association('socrates','professor','filosofia')
s = Subtype('homem','mamifero')
m = Member('socrates','homem')

da = Declaration('descartes',a)
# declara que tem associação a professor de filosofia  
ds = Declaration('darwin',s)
# Decartes declara que é homem e mamifero
dm = Declaration('descartes',m)
# decartes declara que é membro de socrates e homem 

z = SemanticNetwork()
z.insert(da)
z.insert(ds)
z.insert(dm)
z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))
z.insert(Declaration('darwin',Association('homem','gosta','carne')))


# novas declaracoes

z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
z.insert(Declaration('descartes', Member('aristoteles','homem')))

b = Association('socrates','professor','matematica')
z.insert(Declaration('descartes',b))
z.insert(Declaration('simao',b))
z.insert(Declaration('simoes',b))

z.insert(Declaration('descartes', Member('platao','homem')))

e = Association('platao','professor','filosofia')
z.insert(Declaration('descartes',e))
z.insert(Declaration('simao',e))

z.insert(Declaration('descartes',Association('mamifero','altura',1.2)))
z.insert(Declaration('descartes',Association('homem','altura',1.75)))
z.insert(Declaration('simao',Association('homem','altura',1.85)))
z.insert(Declaration('darwin',Association('homem','altura',1.75)))

z.insert(Declaration('descartes', Association('socrates','peso',80)))
z.insert(Declaration('darwin', Association('socrates','peso',75)))
z.insert(Declaration('darwin', Association('platao','peso',75)))


z.insert(Declaration('damasio', Association('filosofo','gosta','filosofia')))
z.insert(Declaration('damasio', Member('socrates','filosofo')))

print("----------------------------------------")
print("List_association")
list = list_association(z)
print(list)
print("----------------------------------------")
print("LIst_objects")
list = list_objects(z)
print(list)
print("----------------------------------------")
print("list_users")
list = list_users(z)
print(list)
print("----------------------------------------")
print("list_types")
list = list_types(z)
print(list)
print("----------------------------------------")
print("list_local_associations")
list = list_local_associations(z, 'socrates')
print(list)
print("----------------------------------------")
print("list_relations_by_user")
list = list_relations_by_user(z, 'descartes')
print(list)
print("----------------------------------------")
print("list_associations_by_user")
list = list_associations_by_user(z, 'decartes')
print(list)
print("----------------------------------------")
print("list_local_associations_by_entity")
list = list_local_associations_by_entity(z, 'socrates')
print(list)
print("----------------------------------------")
print("predecessor")
list = predecessor(z, 'vertebrado','filosofo')
print(list)
print("----------------------------------------")
print("query")
list = query(z, 'vertebrado','socrates')
print(list)

# Extra - descomentar as restantes declaracoes para o exercicio II.2.15

#z.insert(Declaration('descartes', AssocNum('socrates','pulsacao',51)))
#z.insert(Declaration('darwin', AssocNum('socrates','pulsacao',61)))
#z.insert(Declaration('darwin', AssocNum('platao','pulsacao',65)))

#z.insert(Declaration('descartes',AssocNum('homem','temperatura',36.8)))
#z.insert(Declaration('simao',AssocNum('homem','temperatura',37.0)))
#z.insert(Declaration('darwin',AssocNum('homem','temperatura',37.1)))
#z.insert(Declaration('descartes',AssocNum('mamifero','temperatura',39.0)))

#z.insert(Declaration('simao',Association('homem','gosta','carne')))
#z.insert(Declaration('darwin',Association('homem','gosta','peixe')))
#z.insert(Declaration('simao',Association('homem','gosta','peixe')))
#z.insert(Declaration('simao',Association('homem','gosta','couves')))

#z.insert(Declaration('damasio', AssocOne('socrates','pai','sofronisco')))
#z.insert(Declaration('darwin', AssocOne('socrates','pai','pericles')))
#z.insert(Declaration('descartes', AssocOne('socrates','pai','sofronisco')))

# print(z)


