#encoding: utf8

# YOUR NAME: Tiago Pereira
# YOUR NUMBER:98360

# COLLEAGUES WITH WHOM YOU DISCUSSED THIS ASSIGNMENT (names, numbers):
# - Afonso Rodrigues, 107715
# - ...

from semantic_network import *
from constraintsearch import *
import time
class MySN(SemanticNetwork):

    def __init__(self):
        SemanticNetwork.__init__(self)
        self.query_result = None
        self.assoc_stats = {}
        pass

    # def query_local(self,user=None,e1=None,rel=None,e2=None):
    #     # IMPLEMENT HERE
    #     pass
    #     return self.query_result # Your code must leave the output in
    #                       # self.query_result, which is returned here

    def query_local(self, user=None, e1=None, rel=None, e2=None):
        self.query_result = []
        for u, relations in self.declarations.items():
            if user is not None and u != user:
                continue
            for (entity1, relation_name), entity2_or_set in relations.items():
                if e1 is not None and entity1 != e1:
                    continue
                if rel is not None and relation_name != rel:
                    continue
                if e2 is not None:
                    if isinstance(entity2_or_set, set):
                        if e2 not in entity2_or_set:
                            continue
                    else:
                        if entity2_or_set != e2:
                            continue
                relations_n = self.declarations[u][(entity1, relation_name)]
                
                if type(relations_n) == str:
                    self.query_result.append(Declaration(u, Relation(entity1, relation_name, relations_n)))
                else:
                    for r in relations_n:
                        self.query_result.append(Declaration(u, Relation(entity1, relation_name, r)))
                
        return self.query_result

    def query(self, entity, assoc_name=None):
        local = self.query_local(e1=entity)
        assoc = []
        for e2 in [d.relation.entity2 for d in local]:
            assoc.extend(self.query(e2, assoc_name))
        local_assoc = self.query_local(e1=entity, rel=assoc_name)
        self.query_result = assoc + local_assoc
        return self.query_result


    # def query(self,entity,assoc=None):
    #     # IMPLEMENT HERE
    #     pass
    #     return self.query_result # Your code must leave the output in
    #                       # self.query_result, which is returned here

    def find_associated_types(self, entity1, user):
        
        types = set()
        assoc_list = self.query_local(user=user, e1=entity1, rel='member') + \
                    self.query_local(user=user, e1=entity1, rel='subtype')
        for x in assoc_list:
            types.add(x.relation.entity2)
            additional_types = self.find_associated_types(x.relation.entity2, user)
            if additional_types:
                types.update(additional_types)

        return types if types else None

 
    def update_assoc_stats(self,assoc,user=None):
        ldecl = []
        self.assoc_stats.setdefault((assoc, user), ({}, {}))
        for decl in self.query_local(user=user, rel=assoc):
            if not isinstance(decl.relation, Subtype) and not isTypeName(decl.relation.entity1) and not isTypeName(decl.relation.entity2):
                ldecl.append(decl)

        freq1 = {}
        freq2 = {}
        unknown = [0,0]
        for decl in ldecl:
            if self.find_associated_types(decl.relation.entity1, user):
                for types in self.find_associated_types(decl.relation.entity1, user):
                    if types not in freq1:
                        freq1[types] = 1
                    else:
                        freq1[types] += 1
            else:
                unknown[0] += 1
            if self.find_associated_types(decl.relation.entity2, user):
                for types in self.find_associated_types(decl.relation.entity2, user):
                    if types not in freq2:
                        freq2[types] = 1
                    else:
                        freq2[types] += 1
            else:
                unknown[1] += 1
        denominator1 = len(ldecl) - unknown[0] + unknown[0] ** 0.5
        denominator2 = len(ldecl) - unknown[1] + unknown[1] ** 0.5
        for type_key, count in freq1.items():
            self.assoc_stats[(assoc, user)][0][type_key] = count / denominator1

        for type_key, count in freq2.items():
            self.assoc_stats[(assoc, user)][1][type_key] = count / denominator2
        
        return self.assoc_stats



class MyCS(ConstraintSearch):

    def __init__(self,domains,constraints):
        ConstraintSearch.__init__(self,domains,constraints)
        self.calls = 0
        self.solutions = []

    def search_all(self,domains=None):
        self.calls += 1 
        
        if domains==None:
            domains = self.domains

        # se alguma variavel tiver lista de valores vazia, falha
        if any([lv==[] for lv in domains.values()]):
            return None

        # se nenhuma variavel tiver mais do que um valor possivel, sucesso
        if all([len(lv)==1 for lv in list(domains.values())]):
            # se valores violam restricoes, falha
            # ( verificacao desnecessaria se for feita a propagacao
            #   de restricoes )
            # for (var1,var2) in self.constraints:
            #     constraint = self.constraints[var1,var2]
            #     if not constraint(var1,domains[var1][0],var2,domains[var2][0]):
            #         return None 
            return { v:lv[0] for (v,lv) in domains.items() }
       
        # continuação da pesquisa
        # ( falta fazer a propagacao de restricoes )
        for var in domains.keys():
            dom = domains.copy()
            if len(domains[var])>1 :
                for val in dom[var]:
                    newdomains = dict(dom)
                    newdomains[var] = [val]
                    ledges = [ (v, z) for (v, z) in self.constraints if z == var ]
                    newdomains = self.constraint_propagation(newdomains, ledges)
                    solution = self.search_all(newdomains)

                    if solution != None:
                        self.solutions.append(solution)

        return self.solutions

    def constraint_propagation(self, domains, ledges):
        while ledges != []:
            (xj, xi) = ledges.pop()
            numvals = len(domains[xj])
            c = self.constraints[xj, xi]

            domains[xj] = [ val_j for val_j in domains[xj] 
                            if any(c(xj, val_j, xi, val_i) for val_i in domains[xi]) ]

            if len(domains[xj]) < numvals:
                ledges += [ (xk, z) for (xk, z) in self.constraints if z == xj ]
        return domains


