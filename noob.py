# BOOLEAN

# Aufgabe1 Was kostet ein Ticket Varinate 2 und was kosten alle Tickets
'''
Meine VERSION und Fehler

x = input("Bitte gebe an für welche Gruppe du ein Ticket haben möchtest: ")
print(x)

Kinder = str("Kinderpreis 5.00 EUR")
Erwachsene = str("Erwachsene 10.00 EUR")
Senioren = str("Senioren 7.50 EUR")

if  input() == Kinder:
    print("Kinderpreis 5,00 EUR")
    elif input()== Erwachsene:
    print("Erwachsene 10,00 EUR")

else input()== Senioren:
    print("Seniorenpreis 7,50 EUR")
'''



# VERSION von CHATGPT

# BOOLEAN

# Aufgabe 1: Was kostet ein Ticket Variante 2 und was kosten alle Tickets

# Eingabe vom Benutzer
x = input("Bitte gib an, für welche Gruppe du ein Ticket haben möchtest (Kinder, Erwachsene, Senioren): ")
print("Du hast gewählt:", x)

# Bedingungen prüfen
if x == "Kinder":
    print("Kinderpreis: 5,00 EUR")
elif x == "Erwachsene":
    print("Erwachsenenpreis: 10,00 EUR")
elif x == "Senioren":
    print("Seniorenpreis: 7,50 EUR")
else:
    print("Ungültige Eingabe. Bitte gib Kinder, Erwachsene oder Senioren ein.")




'''
| Problem im Original                    | Verbesserung             | Erklärung                                                                  |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------------- |
| `if input() == Kinder`                 | `x == "Kinder"`          | Du brauchst **nur eine Eingabe**, speichere sie in `x`.                    |
| `elif` falsch eingerückt               | Richtig eingerückt       | `elif` darf nicht im Block des vorherigen `if` stehen.                     |
| `else input()== Senioren:`             | `elif x == "Senioren"`   | `else` **darf keine Bedingung** haben. Für Bedingungen benutzt man `elif`. |
| Vergleich mit `"Kinderpreis 5.00 EUR"` | Vergleich mit `"Kinder"` | Du willst mit dem Gruppennamen vergleichen, nicht mit dem ganzen Satz.     |


'''
# Aufgabe 2 von ChatGpt

# Ticketpreise
preis_kinder = 5.00
preis_erwachsene = 10.00
preis_senioren = 7.50

# Eingabe der Kategorie
kategorie = input("Bitte gib an, für welche Gruppe du ein Ticket haben möchtest (Kinder, Erwachsene, Senioren): ")
kategorie = kategorie.strip()  # entfernt Leerzeichen

# Eingabe der Anzahl
anzahl = input("Wie viele Tickets möchtest du kaufen? ")

# Umwandlung der Anzahl in Zahl
if anzahl.isdigit():
    anzahl = int(anzahl)
else:
    print("Bitte gib eine gültige Anzahl ein (nur Zahlen).")
    exit()

# Berechnung je nach Kategorie
if kategorie == "Kinder":
    gesamtpreis = anzahl * preis_kinder
    print(f"{anzahl} Kindertickets kosten {gesamtpreis:.2f} EUR")
elif kategorie == "Erwachsene":
    gesamtpreis = anzahl * preis_erwachsene
    print(f"{anzahl} Erwachsenentickets kosten {gesamtpreis:.2f} EUR")
elif kategorie == "Senioren":
    gesamtpreis = anzahl * preis_senioren
    print(f"{anzahl} Seniorentickets kosten {gesamtpreis:.2f} EUR")
else:
    print("Ungültige Kategorie. Bitte gib Kinder, Erwachsene oder Senioren ein.")




print("HIER DIE LÖSUNG und das SCRIPT vom Tutorial Aufgabe 1 -  nur mit Zahlen")
alter = int(input ("Wie alt bist du? - Bitte nur Zahl eingeben: "))

if alter > 65: # Mit Senioren anfangen ist einfacher dann braucht mann kann zwischenschritte
    print(7.5)
elif alter >= 18:
    print(10.0)
else:
    print(5)

print("HIER DIE LÖSUNG und das SCRIPT vom Tutorial Aufgabe 2 - mit Summe Ticket - nur mit Zahlen")
alter = int(input ("Wie alt bist du? - Bitte nur Zahl eingeben: "))
anzahl = int(input("Wie viele Ticket möchtest du gerne haben? - nur Zahl eingeben: "))

if alter > 65: # Mit Senioren anfangen ist einfacher dann braucht mann kann zwischenschritte
    print(7.5 * anzahl) # Hier einfach mit neue Variable anzahl mulitiplizieren - FERTISCH
elif alter >= 18:
    print(10.0 * anzahl)
else:
    print(5 * anzahl)
