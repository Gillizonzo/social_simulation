from Agent import Agent

class Environment:
    def __init__(self, max_population, agents, epoch_length):
        self.max_population = max_population
        self.agents = agents
        self.cur_population = len(self.agents)
        self.time = 0
        self.epoch_length = epoch_length

    def reproduce(self):
        for agent in self.agents:
            partner = agent.choose_partner([a for a in self.agents if a != agent])
            if partner and self.cur_population < self.max_population:
                self.agents.append(Agent(agent, partner))
    
    def pass_time(self):
        self.time += 1
        for agent in self.agents: agent.senesce()
    
    def activate_environment(self):
        while self.time <= self.epoch_length:
            self.reproduce()
            self.pass_time()
        
    