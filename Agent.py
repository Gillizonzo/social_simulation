from Gene import Gene
import numpy as np
import random

np.random.seed(42)
random.seed(42)
gene_pool = [Gene(lifespan=val) for val in np.random.randint(1, 100, size=20)]

class Agent:
    id = 0
    def __init__(self, parent_a=None, parent_b=None):
        if not parent_a or not parent_b:
            self.genes = (random.choice(gene_pool), random.choice(gene_pool))
        else:
            self.genes = (parent_a.get_reproductive_gene(), parent_b.get_reproductive_gene())
        self.desirability = int(np.clip(np.mean([self.genes[0].get_desirability(), self.genes[1].get_desirability()]) + random.randint(-40, 40),
                                    0, 100))
        self.partner_pickiness = random.randint(0, 10)
        self.is_alive = True
        self.age = 0
        self.expressed_lifespan = max(np.mean([self.genes[0].get_lifespan(), self.genes[1].get_lifespan()]) + random.randint(-10, 10), 1)
        self.reproductive_cooldown = False
        self.max_children_desired = random.randint(0, 5)
        self.children = 0
        self.id = Agent.id
        Agent.id += 1
        
    def get_reproductive_gene(self):
        if self.genes[0].get_dominance():
            if not(self.genes[1].get_dominance()):
                return self.genes[0]
        else:
            if self.genes[1].get_dominance():
                return self.genes[1]
        return random.choice(self.genes)

    def is_living(self):
        return self.is_alive

    def kill(self):
        self.is_alive = False

    def get_expressed_desirability(self):
        return self.desirability
    
    def get_expressed_lifespan(self):
        return self.expressed_lifespan

    def get_pickiness(self):
        return self.partner_pickiness

    def on_reproductive_cooldown(self):
        return self.reproductive_cooldown
    
    def activate_reproductive_cooldown(self, boolean):
        if boolean:
            self.children += 1
        self.reproductive_cooldown = boolean

    def get_max_desired_children(self):
        return self.max_children_desired
    
    def get_children_produced(self):
        return self.children
    
    def get_id(self):
        return self.id
    
    def choose_partner(self, partners):
        partner_ratings = np.array([np.clip(partner.get_expressed_desirability() + random.randint(-15, 5), 0, 100) for partner in partners])
        potential_partners = np.array(partners)[(partner_ratings < self.desirability + self.partner_pickiness)
                                        & (partner_ratings > self.desirability - self.partner_pickiness)]
        return [(partner.get_id(), partner) for partner in potential_partners]
         

    def senesce(self):
        self.age += 1
        if self.age > self.expressed_lifespan:
            self.is_alive = False
        