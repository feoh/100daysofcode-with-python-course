NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

[ n.title() for n in NAMES ]
[ f"{n.split()[1]} {n.split()[0]}" for n in NAMES ]

TNAMES = [ n.title() for n in NAMES ]
TNAMES
TFIRSTS = [ name.split()[0] for name in TNAMES ]
TFIRSTS


import random

def gen_pairs():
    random.seed()
    pool = len(TFIRSTS)
    
    first_partner_index = round(random.random() * pool)
    second_partner_index = round(random.random() * pool)
    
    first_partner = TFIRSTS[first_partner_index]
    second_partner = TFIRSTS[second_partner_index]
    
    pair = f"{first_partner} pairs up with {second_partner}"
    print(pair)
    yield(pair)
    
    
pairs = gen_pairs()

for _ in range(10):
    next(pairs)