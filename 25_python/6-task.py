# Python tuples

car_brands = ("Toyota", "Honda", "Ford", "BMW", "Audi", "Mercedes", "Volkswagen")

print("Populiariausios automobiliu markes:", car_brands)

print("Pirmoji sarase:", car_brands[0])
print("Paskutine sarase:", car_brands[-1])

index1 = car_brands.index("Toyota")
index2 = car_brands.index("Honda")
index3 = car_brands.index("Ford")
index4 = car_brands.index("BMW")
index5 = car_brands.index("Audi")
index6 = car_brands.index("Mercedes")
index7 = car_brands.index("Volkswagen")

brand = input("Iveskite norimos automobiliu markes pavadinima: ")

if brand == "Toyota":
    print("Marke yra sarase, jos indeksas yra:", index1)
if brand == "Honda":
    print("Marke yra sarase, jos indeksas yra:", index2)
if brand == "Ford":
    print("Marke yra sarase, jos indeksas yra:", index3)
if brand == "BMW":
    print("Marke yra sarase, jos indeksas yra:", index4)
if brand == "Audi":
    print("Marke yra sarase, jos indeksas yra:", index5)
if brand == "Mercedes":
    print("Marke yra sarase, jos indeksas yra:", index6)
if brand == "Volkswagen":
    print("Marke yra sarase, jos indeksas yra:", index7)





