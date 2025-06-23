A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Rinkinys A:", A)
print("Rinkinys B:", B)

A.add(5)
print("Rinkinys A po pridėjimo:", A)

B.remove(6)
print("Rinkinys B po pašalinimo:", B)  

union = A.union(B)
print("A ir B sujungimas:", union)

intersection = A.intersection(B)
print("A ir B vienodos reiksmes:", intersection)

difference = A.difference(B)
print("A ir B skirtumas:", difference)

