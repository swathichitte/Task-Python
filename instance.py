class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
          
    def specs(self):
        return f"{self.brand} {self.model}"

laptop1 = Laptop("Dell", "XPS 13")
laptop2 = Laptop("HP", "Spectre x360" )
laptop3 = Laptop("Apple", "MacBook Air" )
laptop4 = Laptop("Lenovo", "ThinkPad X1" )
laptop5 = Laptop("Asus", "ROG Zephyrus" )
laptop6 = Laptop("Acer", "Swift 3" )
laptop7 = Laptop("MSI", "Stealth 15M" )
laptop8 = Laptop("Samsung", "Galaxy Book" )
laptop9 = Laptop("Microsoft", "Surface Laptop 5" )
laptop10 = Laptop("LG", "Gram 17" )

for i, laptop in enumerate([laptop1, laptop2, laptop3, laptop4, laptop5, laptop6, laptop7, laptop8, laptop9, laptop10], start=1):
    print(f"Laptop {i}: {laptop.specs()}")
