class Monster:
    
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.heath = health
    
    def __str__(self): return f"Monster {self.name} has {self.strength}strength and {self.health} health."

