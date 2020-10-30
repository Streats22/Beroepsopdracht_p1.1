## Deze text based applicatie is gebaseerd op  hoe vluchetlingen
## behandeld worden en welke gevaren hun tegenkomen.
import time
EINDE = "Al lijkt dit een simpel en leuk spel dit is op basis gemaakt van echte vluchtelingen\n iedereen heeft een verhaal dit is het eind van jou verhaal.."
Naam = input("Kies een naam: ")
Char = Naam
budget = 20000
Basis_verhaal = "Jou naam is " + Char + " je werkt al jaren voor de overheid."
time.sleep(1)
Smokkelaar_A = "Samen met je famillie heb je een budget van een smokkelaar vinden gaat lastig worden..."

Basis_verhaal2 = " Na een paar jaar orloog in eigenland komt er een opstand ze gaan voor de overheid\n en alle werknemers jij staat hoog op de lijst!"

Basis_verhaal3 = " Op een feestdag besluit je overuren te draaien om wat extra te verdienen dit blijkt de\n verkeerde keuze te zijn de orginiasite valt aan en je moet ontsnappen of vechten!"
print(Basis_verhaal +  Basis_verhaal2 +  Basis_verhaal3 + "a = Vechten\nb = Alleen vluchten\nc = Vluchten me je famillie" +"jou budget is " + budget)

HoofdKeuze = input()



if HoofdKeuze == "a":
    def Vecht():
        print("Na lang nadenken besluit je terug te vecht dit kan je doen door bij het verzet te gaan\n of vanuit het buurland te vechten tegen het onrecht")
        print("Wat is dit? er ligt iets waar je jezelf mogelijk mee kan beschermen er is A = een object wat op een lamp lijkt\nB = Bare hands! " )
        Keuze_x = input("Waar kies je voor? ")
        if Keuze_x == "B":
            print("Je kiest voor het zelf vechten met je bare hands!")
            time.sleep(1)
            print("Ja het idee is leuk maar hun hebben wapen....")
            print(EINDE)
        elif Keuze_x == "A":
            print("Je moet kiest ervoor om een wapen pakken  de wel genomende lamp ja dat is precies wat je denkt een lamp niets meer")
            print(" na lang vechten heb je met de ijzere lamp 2 vechters kunnen uitschakelen alleen er is een 3e vechter die je uitschakelt met een kogel..")
            print(EINDE)
        else:
            print("Dit is geen juiste invoer")
            time.sleep(3)
    Vecht()


elif HoofdKeuze == "b":
    def Vlucht_alleen():
        print("je heb gekozen om je problemen to ontvluchten  zonder je famillie")
        if Keuze_V == "B":
            print("Je besluit het verzet te dienen in je eigenland")
            time.sleep(1)
            print("Een spion blijkt je gevolgen te hebben van de orginiasite die jou zoekt, je bent ondekt.... REN!!!!")
            time.sleep(0.4)
            print("Ongeacht je pogin om te rennen blijkt dit te vergeefs je wordt door de spoin neer gehaald.. ")
            print(EINDE)
        elif Keuze_V == "A":
            print("Je besluit vanuit het buurland te vechten, dit blijkt een slimme zet het buurland kon\n jou beter beschermen dan je eigenland...")
            print(" deze keuze was misschien wel slim maar ook dit land heeft vechters van dezelfde vijandige orginiasite")
            print(EINDE)
        else:
            print("Dit is geen juiste invoer")
            time.sleep(3)
    Vlucht_alleen()

elif HoofdKeuze == "c":
    def Vlucht_Met_Fam():
        print("Na het lang nadenken kies je voor het vluchten met je famillie.")

        print("Je Komt bij een smokkelaar die jou veder kan helpen dit kost voor jou €6000 je bent met 4 personen. zoek je door of laat je iemand achter?")
        keuze_A = input("Kies wijs.. ")
        if keuze_A == "X":
            print("Je besluit het verzet te dienen in je eigenland")
            time.sleep(1)
            print("Een spion blijkt je gevolgen te hebben van de orginiasite die jou zoekt, je bent ondekt.... REN!!!!")
            time.sleep(0.4)
            print("Ongeacht je pogin om te rennen blijkt dit te vergeefs je wordt door de spoin neer gehaald.. ")
            print(EINDE)
        elif keuze_A == "Y":
            keuze_A == 1
            print("Je laat iemand achter maar wie...")
            if keuze_A == 1:
                keuze_C = input("Wie Blijft achter? ")
                print("Jezelf, Je vrouw, Je dochter of je zoon?")
            elif keuze_C == "V":
                print("Je besluit je vrouw achter te laten")
                print("Ongeacht je pogin om te rennen blijkt dit het dat je vrouw is overgehand aan de orginiasite die je achterna zit... ")
                print(EINDE)
            elif keuze_C == "Z":
                print("Je besluit je zoon achter te laten")
                print("Ongeacht je pogin om te rennen blijkt dit het dat je zoon is overgehand aan de orginiasite die je achterna zit... ")
                print(EINDE)
            elif keuze_C == "D":
                print("Je besluit je dochter achter te laten")
                print("Ongeacht je pogin om te rennen blijkt dit het dat je dochter is overgehand aan de orginiasite die je achterna zit... ")
                print(EINDE)
            elif keuze_C == "J":
                print("Je besluit je zelf achter te blijven")
                print("Ongeacht je pogin om te rennen blijkt dit te vergeefs je wordt door een assasin neer gehaald.. ")
                print(EINDE)
            else:
                print("Dit is geen juiste invoer")
                print(EINDE)
        else:
            print("Dit is geen juiste invoer")
            time.sleep(3)


    Vlucht_Met_Fam()

else:
    print("Dit is geen juiste invoer")
    print(EINDE)
