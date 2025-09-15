class Resturant:
    total_eatery=0
    total_tables = 4
    def __init__(self, name: str,location: str,spectality: str):
        self.name=name
        self.location=location
        self.spectality=spectality
        Resturant.total_eatery+=1


class Eatery(Resturant):
   
    def __init__(self, name, location, spectality,  menu: list):
        super().__init__(name, location, spectality)
        
        self.menu:list[str] = menu


    def order(self, order):
        if Resturant.total_tables >= 1:
            for item in self.menu:
                if item == order:
                    print("Your order will take 2 min to heat up")
                    Resturant.total_tables -=1
                    return f"{order} is Ready"
        else:
            return "Sorry no table Available at the moment"
        
    
        

mrBiggs = Eatery("Mr_Biggs","JOS","African Dishs",["Rice","Bean","Fufu"])
print(mrBiggs.order("Fufu"))
print(mrBiggs.order("Bean"))
print(mrBiggs.order("Rice"))
print(mrBiggs.order("Fufu"))
print(mrBiggs.order("Fufu"))
print(mrBiggs.total_tables)
print(mrBiggs.total_eatery)
            

        