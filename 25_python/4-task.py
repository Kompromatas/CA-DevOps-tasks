# Python list

capitals = ["Vilnius", "Riga", "Tallinn", "Helsinki", "Oslo", "Stockholm", "Copenhagen"]

print("Sostiniu sarasas:", *capitals)

capitals.sort()

print("Sostiniu sarasas po rusiavimo:", *capitals)

capital = input("Iveskite sostine, kuria pridesime prie saraso: ")

capitals.append(capital)
print("Sostiniu sarasas po pridetos sostines:", *capitals)

capitalremove = input("Iveskite sostine, kuri bus istrinta is saraso: ")

capitals.remove(capitalremove)

print("Sostiniu sarasas po istrintos sostines:", *capitals)

capitaladd = input("Iveskite sostine, kuri bus iterpta i 3 vieta: ")

capitals.insert(2, capitaladd)

print("Sostiniu sarasas po iterptos sostines:", *capitals)

