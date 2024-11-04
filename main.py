for i in range(2):
    for adjectif in ["beau", "fort", "con"]:
        if adjectif == "con":
            adjectif = "légendaire"
        elif adjectif == "fort":
            adjectif = "bla"
        else:
            adjectif = "nimp"
        print(f"Thibault est le plus {adjectif}")
    print(1==1)

fruits = ["pomme", "banane", "cerise"]
print(fruits[2])
fruits.append("orange")
print(fruits[3])
