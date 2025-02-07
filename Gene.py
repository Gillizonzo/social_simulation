import random
import numpy as np

np.random.seed(42)
global gene_pool
class Gene:
    id = 1
    def __init__(self, lifespan):
        self.lifespan = lifespan
        self.is_dominant = bool(random.randint(0, 1))
        self.theoretical_desirability = random.randint(0, 100)
        self.expressions = 1
        if self.expressions == 1:
            self.id = Gene.id
            Gene.id += 1
        else:
            self.id = self.id
    
    def get_lifespan(self):
        return self.lifespan

    def get_dominance(self):
        return self.is_dominant
    
    def get_desirability(self):
        return self.theoretical_desirability
    
    def express(self):
        self.expressions += 1
    
    def get_expressions(self):
        return self.expressions
    
    def drop_from_gene_pool(self):
        self.expressions -= 1

    def get_gene_name(self):
        return self.id
    
gene_pool = [Gene(lifespan=val) for val in np.random.randint(1, 100, size=7)]