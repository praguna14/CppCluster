"""class for clusters"""
import observation

class Clusters(object):
    
    def __init__(self, observations):
        self.observations = observations
    
    def add(self, observation):
        self.observations.append(observation)

    def remove(self, observation):
        for i in range(len(self.observations)):
            if self.observations[i] == observation:
                self.observations.remove(self.observations[i])
