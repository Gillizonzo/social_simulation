from Agent import Agent
from Environment import Environment


if __name__ == "__main__":
    agents = [Agent() for _ in range(400)]
    environment = Environment(max_population=3000, agents=agents, epoch_length=75)
    environment.activate_environment()