import matematika

a = input("Iveskite pirma skaiciu: ")
b = input("Iveskite antra skaiciu: ")

print("Skaiciu suma yra:", matematika.sudetis(int(a), int(b)))
print("Skaiciu skirtumas yra:", matematika.atimtis(int(a), int(b)))
print("Skaiciu sandauga yra:", matematika.daugyba(int(a), int(b)))
print("Skaiciu dalyba yra:", matematika.dalyba(int(a), int(b)))

print("Skaiciu sumos ir skirtumo suma yra:", matematika.sudetis(matematika.sudetis(int(a), int(b)), matematika.atimtis(int(a), int(b))) )
print("Skaiciu sandaugos ir dalybos suma yra:", matematika.sudetis(matematika.daugyba(int(a), int(b)), matematika.dalyba(int(a), int(b))) )
