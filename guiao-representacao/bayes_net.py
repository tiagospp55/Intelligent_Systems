from bayes_net import *
import itertools

bn = BayesNet()

variables = ['sc', 'pt', 'cp', 'fr', 'pa', 'cnl']

bn.add('sc', [], 0.6)
bn.add ('pt',[], 0.05)

bn.add('cnl',[('sc', True)], 0.9)
bn.add('cnl', [('sc', False)], 0.001)

bn.add('pa',[('pt', True)], 0.25)
bn.add('pa',[('pt', False)], 0.04)

bn.add('cp',[('sc', True), ('pa', True)], 0.02)
bn.add('cp',[('sc', True), ('pa', False)], 0.01)
bn.add('cp',[('sc', False), ('pa', True)], 0.011)
bn.add('cp',[('sc', False), ('pa', False)], 0.001)

bn.add('fr',[('pa', True), ('pt', True)], 0.9)
bn.add('fr',[('pa', True), ('pt', False)], 0.1)
bn.add('fr',[('pa', False), ('pt', True)], 0.9)
bn.add('fr',[('pa', False), ('pt', False)], 0.01)

for l in itertools.product({True, False}, repeat=5):
    print(bn.jointProb(zip(variables, l)))
