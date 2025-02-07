from Agent import Agent
import Gene
import random
import pandas as pd

seed = 42
random.seed(seed)
pre_df_pop_data = []
pre_df_gene_data = []
class Environment:
    def __init__(self, max_population, agents, epoch_length):
        self.max_population = max_population
        self.agents = agents
        self.cur_population = len(self.agents)
        self.deaths = 0
        self.births = 0
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
                    if (self.cur_population < self.max_population and 
                        (not(cur_agent.on_reproductive_cooldown()) and not(pot_partner.on_reproductive_cooldown())) and
                        (cur_agent.get_children_produced() < min(cur_agent.get_max_desired_children(), pot_partner.get_max_desired_children()) and 
                        (pot_partner.get_children_produced() < min(cur_agent.get_max_desired_children(), pot_partner.get_max_desired_children())))):

                        self.agents.append(Agent(cur_agent, pot_partner))
                        cur_agent.activate_reproductive_cooldown(True)
                        pot_partner.activate_reproductive_cooldown(True)
                        self.cur_population += 1
                        self.births += 1
            agent_i += 1

    
    def pass_time(self):
        self.time += 1
        new_agents = []
        for agent in self.agents: 
            agent.senesce()

            dist = [False for _ in range(19)]
            dist[0] = True
            if random.choice(dist):
                agent.kill() 

            if not(agent.is_living()):
                self.cur_population -= 1
                self.deaths += 1
            else:
                new_agents.append(agent)
        self.agents = new_agents
    
    def activate_environment(self):
        while self.time <= self.epoch_length:
            self.reproduce()
            self.pass_time()
            for agent in self.agents:
                agent.activate_reproductive_cooldown(False)
            self.get_statistics()
        pd.DataFrame(pre_df_pop_data).to_csv(f'simulation_pop_results_{seed}.csv')
        pd.DataFrame(pre_df_gene_data).to_csv(f'simulation_gene_results_{seed}.csv')
        
    def get_statistics(self):
        average_lifespan = 0
        average_desirability = 0
        
        for agent in self.agents:
            average_lifespan += agent.get_expressed_lifespan()
            average_desirability += agent.get_expressed_desirability()

        average_lifespan /= self.cur_population + 10e-7
        average_desirability /= self.cur_population + 10e-7
        print(f'Time: {self.time} | Current Population: {self.cur_population} | Births: {self.births} | Deaths: {self.deaths} | Average Lifespan: {average_lifespan} | Average Desirability: {average_desirability}')
        gene_distribution = []
        for gene in Gene.gene_pool:
            gene_distribution.append((gene.get_gene_name(), gene.get_expressions()))
        pop_data = {'Time': self.time,
                'Current Population' : self.cur_population,
                'Births' : self.births,
                'Deaths' : self.deaths,
                'Average Lifespan' : average_lifespan,
                'Average Desirability' : average_desirability}
        gene_dist_data = {'Time': self.time} | {f'Gene {gene_name}' : num_expressions for gene_name, num_expressions in gene_distribution}
        pre_df_pop_data.append(pop_data)
        pre_df_gene_data.append(gene_dist_data)
    