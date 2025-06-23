# Python dictionaries

student = {"Vardas": "Jonas", "Amzius": 20, "Grade level": "A"}

print("Studento informacija:")
print(student)

programa = input("Iveskite studento studiju programa: ")
student["Programa"] = programa
pazymys = input("Iveskite studento pazymi: ")
student["Pazymys"] = pazymys

print("Atnaujinta studento informacija:")
print(student)