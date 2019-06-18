NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def gen_pairs():
    first_names = [ name.split()[0].title() for name in NAMES ]
    
    while True:
        first, second = None, None
        
        while first == second:
            first, second = random.sample(first_names, 2)

        pairs = f"{first} pairs with {second}"
        yield(pairs)
    

pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))


