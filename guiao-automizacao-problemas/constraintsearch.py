# # Pesquisa para resolucao de problemas de atribuicao
# # 
# # Introducao a Inteligencia Artificial
# # DETI / UA
# #
# # (c) Luis Seabra Lopes, 2012-2019
# #


from itertools import products
# variables = ['A', 'B', 'C', 'D', 'E', 'F']
# # columns = [1,2,3,4]
# # domains = {v: columns for v in variables}
# edges = [ (v1,v2) for v1 in variables
# 		  for v2 in variables if v1 != v2]
		  
# colours = ['a','b','c','d','e', 'f']
# domains = {v: colours for v in variables }
# constraints = {e : no_attack for e in edges}

# def no_attack(v1,x1,v2,x2):

# 	if x1 == x2:
# 		return False
# 	r1 = int(v1[1:])
# 	r2 = int(v2[2:])
	
# 	if abs(r1-r2) == abs(x1-x2) :
# 		return False
# 	return True

# class ConstraintSearch:

#     # domains é um dicionário com o domínio de cada variável;
#     # constaints e' um dicionário com a restrição aplicável a cada aresta;
#     def __init__(self,domains,constraints):
#         self.domains = domains
#         self.constraints = constraints
#         self.calls = 0

#     # domains é um dicionário com os domínios actuais
#     # de cada variável
#     # ( ver acetato "Pesquisa com propagacao de restricoes
#     #   em problemas de atribuicao - algoritmo" )
#     def search(self,domains=None):
#         self.calls += 1 
        
#         if domains==None:
#             domains = self.domains

#         # se alguma variavel tiver lista de valores vazia, falha
#         if any([lv==[] for lv in domains.values()]):
#             return None

#         # se nenhuma variavel tiver mais do que um valor possivel, sucesso
#         if all([len(lv)==1 for lv in list(domains.values())]):
#             # se valores violam restricoes, falha
#             # ( verificacao desnecessaria se for feita a propagacao
#             #   de restricoes )
#             for (var1,var2) in self.constraints:
#                 constraint = self.constraints[var1,var2]
#                 if not constraint(var1,domains[var1][0],var2,domains[var2][0]):
#                     return None 
#             return { v:lv[0] for (v,lv) in domains.items() }
       
#         # continuação da pesquisa
#         # ( falta fazer a propagacao de restricoes )
#         for var in domains.keys():
#             if len(domains[var])>1:
#                 for val in domains[var]:
#                     newdomains = dict(domains)
#                     newdomains[var] = [val]
#                     solution = self.search(newdomains)
#                     if solution != None:
#                         return solution
#         return None


# cs = ConstraintSearch(domains, constraints)
# print(cs.search())





# ## Amigos são as variaveis
# # A pessoa A pode levar bicicleta de B, e chapeu de C ou bicicleta de C e chapeu de B



vairables = ['q1', 'q2', 'q3', 'q4']
columns = [1,2,3,4]
domains = {v: columns for v in variables}


#      	      qi c1 qj cj
def no_attack(v1,x1,v2,x2):

	if x1 == x2:
		return False
	r1 = int(v1[1:])
	r2 = int(v2[2:])
	
	if abs(r1-r2) == abs(x1-x2) :
		return False
	return True
	
edges = [ (v1,v2) for v1 in variables
		  for v2 in variables if v1 != v2]
		  
constraints = {e : no_attack for e in edges}
	 
Class ConstraintSearch:
	def __init__(self, domains, constrints):
		self.domain = domains
		self.constraints = constraints
		
	def search(self, varvals,....
	
		if varvals == None:
			varvals = self.domains 
		#check if thre is an empty domain 
		
		if any(varsvals[v] == [] for v in varsvals):
			return None
			
		
		# check if all doamins have exactly one value 
		if all(len(varvals[v]) == for v in vasvals):
			# check constraints
			solution = {v: varsvals[v][0] for v in varvals}	
			return solution
			
		for v in varvals:
			if len(varvals[v] > 1:
				for x in varvals[v]:
					newvarvals = {**varvals}
					varvals[v] = [x]
					
					solution = self.search(newvarvals)
					if solution != None
						return solution
						
				
		# otherwise we will have a for loop
		# for loop whith a recursive call to the self.search() function
	
    variables = ['T','W','O','F','U','R']

    digits = list(range(10))

    domains = {v:digits for v in variables if v!= 'F'}

    domains |= {v:[0,1] for v un ['X1','X2','F']}

    domains['ORX1'] = product(domains['O'], domains['R'], domains['X1'])
    domains['RX1'] = [t for t in domains['ORX1'] if 2*t[0] == t[1] + 10*t[2]]
# domains for two-more constraints (add here)

    tupleconstraint0 = lamda tv,tx,v,x: t[0] == x
    tupleconstraint1 = lamda tv,tx,v,x: t[0] == x
    tupleconstraint2 = lamda tv,tx,v,x: t[0] == x
    tupleconstraint3 = lamda tv,tx,v,x: t[0] == x
    
    extra = {}
    extra['ORX1','O'] = tupleconstraint0
    extra['ORX1','R'] = tupleconstraint1
    extra['ORX1','X1'] = tupleconstraint2

# Two more extra constraints 
    constraints |= extra
    constraints |= {(v2,v1):lambda w2,x2,w1,x1: extra[w2,x2,w1,x1] for v1,v2 in extra}

print(constraints)




