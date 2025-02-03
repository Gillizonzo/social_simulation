from Agent import Agent

class Environment:
    def __init__(self, max_population, agents, epoch_length):
        self.max_population = max_population
        self.agents = agents
        self.cur_population = len(self.agents)
        self.deaths = 0
        self.time = 0
        self.epoch_length = epoch_length

    def reproduce(self):
        relationship_graph = {}
        for agent in self.agents:
            relationship_graph[agent.get_id()] = agent.choose_partner(partners=[a for a in self.agents if a != agent])

        agent_i = 0
        for agent_id, id_partner_tuples in relationship_graph.items():
            for id, pot_partner in id_partner_tuples:
                if agent_id in [tup[0] for tup in relationship_graph.get(id, [])]:
                    cur_agent = self.agents[agent_i]
                    if (pot_partner and 
                        self.cur_population < self.max_population and 
                        (not(cur_agent.on_reproductive_cooldown()) and not(pot_partner.on_reproductive_cooldown())) and
                        (cur_agent.get_children_produced() < min(cur_agent.get_max_desired_children(), pot_partner.get_max_desired_children()) and 
                        (pot_partner.get_children_produced() < min(cur_agent.get_max_desired_children(), pot_partner.get_max_desired_children())))):

                        self.agents.append(Agent(cur_agent, pot_partner))
                        cur_agent.activate_reproductive_cooldown(True)
                        pot_partner.activate_reproductive_cooldown(True)
                        self.cur_population += 1

    
    def pass_time(self):
        self.time += 1
        for agent in self.agents: 
            agent.senesce()
            if not(agent.is_alive()):
                self.cur_population -= 1
                self.deaths += 1
    
    def activate_environment(self):
        while self.time <= self.epoch_length:
            self.reproduce()
            self.pass_time()
        for agent in self.agents():
            agent.set_reproductive_cooldown(False)
        self.get_statistics()
        
    def get_statistics(self):
        average_lifespan = 0
        average_desirability = 0
        
        for agent in self.agents():
            average_lifespan += agent.get_expressed_lifespan()
            average_desirability += agent.get_expressed_desirability()

        average_lifespan /= self.cur_population
        average_desirability /= self.cur_population
        print(f'Time: {self.time} | Average Lifespan: {average_lifespan} | Average Desirability: {average_desirability}')

    