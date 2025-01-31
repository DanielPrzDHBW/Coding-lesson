class Player:
    
    def __init__(self, name, strength):
        self.name = name
        self.health = 100
        self.strength = strength

    def __str__ (self): return f"Player {self.name} has {self.strength} strength and {self.health} health."
    
    def take_damage(self, damage): self.health -= damage
    
    def regain_health(self, health_regain): 
        self.health += health_regain
        if self.health > 100: self.health = 100

    