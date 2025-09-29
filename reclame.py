from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro.")

aanbieding_1("aardbei", 4, 0.1)

inkomsten = [220, 430, 125, 160, 90, 345]

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

totaal = inkomsten_totaal(inkomsten)
BTW = 0.09 * totaal
print(f"het totaal van alle inkomsten van deze week is {totaal} euro, waarover {BTW:.2f} euro btw betaald dient te worden")

weekinkomsten = [220, 430, 125, 160, 205, 90, 345]

def min_en_max(weekinkomen):
    return max(weekinkomen), min(weekinkomen)

def gemiddelde(weekinkomen):
    return sum(weekinkomen) / len(weekinkomen)

print(f"De hoogste en laagste inkomsten van deze week zijn: {min_en_max(weekinkomsten)}")  # Output: (430, 90)
print(f"De gemiddelde inkomsten van deze week zijn {gemiddelde(weekinkomsten):.2f} euro")  # Output: 220.71 euro

def mijn_functie(meervoudig):
    invoer_lijst = {10,5,3,2,1,2,9}
    return hoog_en_laagste(invoer_lijst)


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer


