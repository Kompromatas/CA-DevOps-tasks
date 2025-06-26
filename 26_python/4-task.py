numbers = input("Iveskite sveikuosius skaicius atskirtus tarpu: ")

print("Ivesti skaiciai: ", numbers)

numbers_list = numbers.split()

bigest_number = max(numbers_list)    
smallest_number = min(numbers_list) 

print("Didziausias skaicius: ", bigest_number)
print("Mažiausias skaicius: ", smallest_number)