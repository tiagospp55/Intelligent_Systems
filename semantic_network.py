

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1 # Membro
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2 
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl


    def __str__(self):
        return str(self.declarations)
    
    def insert(self,decl):
        self.declarations.append(decl)
    
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))


# Exercicio 1 
def list_association(self):
    return [d.relation.name for d in self.declarations if type(d.relation) == Association]

# Exercicio 2
def list_infered_objects(self):
    return [d.relation.entity1 for d in self.declarations if type(d.relation) == Member]

# Exercicio 3
def list_users(self):
    return [d.user for d in self.declarations]

# Exercicio 4
def list_types(self):
    list = []
    for d in self.declarations:
        if type(d.relation) == Association:
            list.append(d.relation.entity1)
            list.append(d.relation.entity2)
        if type(d.declarations) == Subtype:
            list.append(d.subtype.supertype)
    return list

# Exercicio 5
def list_local_associations(self, entity):
    return [d.relation.name for d in self.declarations if entity == d.relation.entity1 and type(d.declarations)]


# Exercicio 6
def list_relations(self, user):
    return [d.relation.name for d in self.declarations if self.user == user]

#Exercicio 7
def len_association(self, user):
    return len(list_local_associations(user))

# Exercicio 8
def list_tuples(self, entity):
    list_t = []

    for d in self.declarations:
        if d.relation.entity1 == entity or d.relation.entity2 == entity:
            list.append((d.user, d.relation.name))

    return list        

# Exercicio 9
def predecessor(self, pre, pos):
    for d in self.declarations:
        if type(d.relation) == Member or type(d.relation) == Subtype:
            if d.relation.entity2 == pre and d.relation.entity1 == pos:
                return True
            if d.relation.entity1 == pos:
                return self.predecessor(pre, d.relation.entity2)
            
    return False

# Exercicio 10

def predecessor_path(self,e1,e2, list):
    if predecessor(e1,e2) == False:
        return None
    
    for d in d.declarations:
        if type(d.relation) == Member or type(d.relation) == Subtype:
            if d.relation.entity2 == e1 and d.relation.entity1 == e2:
                return [list + d.relation.entity2]
            if d.relation.entity1 == e2:
                return [list + predecessor_path(e1, d.relation.entity2)] 
    return None

# Exercicio 11A


def query(self, entity, association_name=None):
    ldeclartions = self.query_local(e1=entity)
    lparents = [ d.relation.entity2 for d in ldeclartions if not isinstance(d.relation, Association) ]

    lassoc = [ d for d in ldeclartions if isinstance(d.relation, Association) 
                                        and (d.relation.name == association_name or association_name == None) ]
    
    for p in lparents:
        lassoc += self.query(p, association_name)
    return lassoc


# Exercicio 11B

def query2(self, entity, relation_name=None):
    query_result = self.query(entity)

    ldeclartions = self.query_local(e1=entity)
    lassoc = [ d for d in ldeclartions if not isinstance(d.relation, Association) 
                                        and (d.relation.name == relation_name or relation_name == None) ]

    return query_result + lassoc


# Exercicio 12

def query_cancel(self, entity, association_name):
    ldeclartions = self.query_local(e1=entity)
    lparents = [ d.relation.entity2 for d in ldeclartions if not isinstance(d.relation, Association) ]

    lassoc = [ d for d in ldeclartions if isinstance(d.relation, Association) and d.relation.name == association_name ]
    
    if lassoc == []:
        for p in lparents:
            lassoc += self.query_cancel(p, association_name)


    return lassoc


# Exercicio 13

def query_down(self, entity, association_name, child=False):
    ldeclartions = self.query_local(e2=entity)
    lchildren = [ d.relation.entity1 for d in ldeclartions if not isinstance(d.relation, Association) ]

    lassoc = []
    if child:
        lassoc = [ d for d in self.query_local(e1=entity) if isinstance(d.relation, Association) 
                                                            and d.relation.name == association_name ]

    for c in lchildren:
        lassoc += self.query_down(c, association_name, child=True)

    return lassoc

# Exercicio 14
def query_induce(self, entity, association_name):
    lassoc = self.query_down(entity, association_name)

    counter_dict = {}

    for assoc in lassoc:
        if assoc.relation.entity2 not in counter_dict:
            counter_dict[assoc.relation.entity2] = 1
        else:
            counter_dict[assoc.relation.entity2] += 1
    
    return max(counter_dict, key=counter_dict.get)

# Exercicio 15
def query_local_assoc(self, entity, association_name):
    ldeclartions = self.query_local(e1=entity)
    print(ldeclartions)
    # for d in ldeclartions:
    #     print(d)







































