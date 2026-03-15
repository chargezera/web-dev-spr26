class ComputerPart:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):
        return f"{self.brand} {self.model} costs ${self.price}"
    
    def get_power_info(self):
        return "This computer part uses standard power."
    
    def __str__(self):
        return f"Part: {self.brand} {self.model}, Price: ${self.price}"
    
class CPU(ComputerPart):
    def __init__(self, brand, model, price, cores):
        super().__init__(brand, model, price)
        self.cores = cores

    def get_info(self):
        return f"CPU: {self.brand} {self.model}, {self.cores} cores, Price: ${self.price}"
    
    def get_power_info(self):
        return f"CPU Power usage is optimized for {self.cores} cores."
    
class GPU(ComputerPart):
    def __init__(self, brand, model, price, vram):
        super().__init__(brand, model, price)
        self.vram = vram

    def get_info(self):
        return f"GPU: {self.brand} {self.model}, {self.vram}GB VRAM, Price: ${self.price}"
    
    def get_power_info(self):
        return f"GPU requires higher power for {self.vram}GB RAM."