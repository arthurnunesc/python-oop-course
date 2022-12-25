class Bacterium:
    def __init__(self, size, shape, forms_endospores, is_beneficial, antibiotic_resistances, x, y):
        self.size = size
        self.shape = shape
        self.forms_endospores = forms_endospores
        self.is_beneficial = is_beneficial
        self.antibiotic_resistances = antibiotic_resistances
        self.x = x
        self.y = y


# Create 3 instances
bacteria1 = Bacterium(50, "Bacili", True, True, None, 0, 0)
bacteria2 = Bacterium(100, "Cocci", False, False, "Paracetamol", -10, 1)
bacteria3 = Bacterium(20, "Spirilli", False, True, "Ibuprofen, Penicilin", 99, 33)
