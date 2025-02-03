from Gene import Gene
import numpy as np
import random

gene_pool = [Gene(age=val) for val in np.random.randint(1, 100, size=20)]

class Agent:
    def __init__(self, parent_a=None, parent_b=None):
        if not parent_a or not parent_b:
            self.genes = (random.choice(gene_pool).copy(), random.choice(gene_pool).copy())
        else:
            self.genes = (parent_a.get_reproductive_gene(), parent_b.get_reproductive_gene())
        self.desirability = np.clip(np.mean(self.genes[0].get_desirability(), self.genes[1].get_desirability()) + random.randint(-20, 20),
                                    0, 100)
        
        def get_reproductive_gene(self):
            if self.genes[0].get_dominance():
                if not(self.genes[1].get_dominance()):
                    return self.genes[0]
            else:
                if self.genes[1].get_dominance():
                    return self.genes[1]
            return random.choice(self.genes)

        def get_expressed_desirability(self):
            return self.desirability
        
        def choose_partner(self, partners):
            return np.argmax([np.clip(partner.get_expressed_desirability() + random.randint(-15, 15), 0, 100) for partner in partners])