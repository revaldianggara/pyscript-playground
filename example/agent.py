class Agent:
    def __init__(self, name, demage, meta, weapon):
        self.name = name
        self.demage = demage
        self.meta = meta
        self.weapon = weapon
    
    def get_name(self):
        return f"Hi, my name is {self.name}, "

    def get_demage(self):
        return f"{self.name} damage is {self.demage}, "

    def get_meta(self):
        if(self.meta):
            return f"i'm meta for now, "
        else:
            return f"i'm not meta right now, "

    def get_weapon(self):
        return f"my best weapon {self.weapon}, "

    def get_all_data(self):
        return f"{self.get_name()} {self.get_demage()} {self.get_meta()} {self.get_weapon()}"