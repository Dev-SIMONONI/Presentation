from Eatery import Resturant, Eatery

mrBiggs = Eatery("Mr_Biggs","JOS","African Dishs",["Rice","Bean","Fufu"])
print(mrBiggs.order("Fufu"))
print(mrBiggs.order("Bean"))
print(mrBiggs.order("Rice"))
print(mrBiggs.order("Fufu"))
print(mrBiggs.order("Fufu"))
print(mrBiggs.total_tables)
print(mrBiggs.total_eatery)