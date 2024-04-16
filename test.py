           #0      #1         #2       #3        #4       #5        #6       #7
zbozi = ["Audi", "Skoda", "Mercedes", "BMW", "Porsche", "Honda", "Subaru", "Mazda"]

koosik = []

print("Vitejte v nasim obchode Auta-smysl naseho zivota! Zde si muzete vybrat produkt z naseho zbozi ")


def vypis_zbozi(zbozi):
    for x in range(len(zbozi)):
        print(f"{x+1}{zbozi[x]}")


def vypis_koosik(koosik):
    for x in range(len(koosik)):
        print(f"{x+1}{koosik[x]}")


print("Zde si muzete vybrat produkt z naseho zbozi")
print("Vybirat muzete pomoci nazvu nebo cisla")
print("Pro ukonceni zadejte prikaz dost")


for x in range(len(zbozi)):


    print("Nabidka:")

    vypis_zbozi(zbozi)

    cislo_zbozi = int(input("cislo.zbozi:"))

    koosik.append(zbozi[cislo_zbozi-1])

    zbozi.remove(zbozi[cislo_zbozi-1])

    vypis_zbozi(zbozi)

    print("vas kosik:")

    vypis_koosik(koosik)


 

