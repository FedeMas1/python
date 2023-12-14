pizza=input("Quiere una pizza vegetariana? ")

if pizza == "si" :
    ingrediente=input("Elija su ingrediente entre Espiaca y tofu ")
    print("La pizza tiene Mozzarella, tomate y ", ingrediente)
elif pizza == "no":
    ingrediente= input("Elija un ingrediente entre pepperoni, jamon y huevo ")
    print("La pizza tiene mozzarella, tomate y ", ingrediente)