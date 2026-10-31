# Einfache Listenverwaltung für die Konsole

liste = []

while True:
    eingabe = input(
        "Aufgabe: anzeigen = a / hinzufügen = h / entfernen = e / beenden = b: "
    )
    while eingabe not in ["a", "h", "e", "b"]:
        eingabe = input(
            "Fehler! Aufgabe: anzeigen = a / hinzufügen = h / "
            "entfernen = e / beenden = b: "
        )

    if eingabe == "a":
        print(liste)
    elif eingabe == "h":
        while True:
            eintrag = input("Was möchtest du hinzufügen? (b = zurück): ")
            if eintrag.lower() == "b":
                break
            elif eintrag in liste:
                print("Fehler! Dieser Eintrag ist bereits in der Liste.")
            else:
                liste.append(eintrag)
    elif eingabe == "e":
        while True:
            aktion = input(
                "Alles entfernen = a / Eine Sache entfernen = e / Zurück = b: "
            )
            if aktion not in ["a", "e", "b"]:
                print("Fehler! Bitte a, e oder b eingeben.")
            elif aktion == "a":
                liste.clear()
                print("Die Liste wurde geleert.")
                break
            elif aktion == "e":
                while True:
                    eintrag = input("Was möchtest du löschen? (z = zurück): ")
                    if eintrag.lower() == "z":
                        break
                    elif eintrag in liste:
                        liste.remove(eintrag)
                        print(eintrag, "wurde gelöscht.")
                    else:
                        print("Fehler! Dieser Eintrag ist nicht in der Liste.")
                        print(liste)
            else:
                break
    else:
        break

print("----- Programm beendet -----")
