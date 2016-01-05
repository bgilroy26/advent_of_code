class Reindeer():
    def __init__(self, name, speed, endurance, refractory):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.refractory = refractory
        self.dash_and_recover = endurance + refractory
        self.distance = 0
        self.points = 0

    def run(self, seconds):
        wind = seconds % self.dash_and_recover
        if wind <= self.endurance:
            self.distance += self.speed
            
        
