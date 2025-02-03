from Agent import Agent
from Environment import Environment


if __name__ == "__main__":
    agents = [Agent() for _ in range(200)]
    environment = Environment(max_population=1000, agents=agents, epoch_length=75)
    environment.activate_environment()