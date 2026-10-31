x = []

while True:
    eingabe = input("Aufgabe: anzeigen = a / hinzufügen = h / entfernen = e / beenden = b: ")
    while eingabe not in ["a", "h", "e", "b"]:
        eingabe = input("Fehler! Aufgabe: anzeigen = a / hinzufügen = h / entfernen = e / beenden = b: ")
    if eingabe == "a":
        print(x)
    elif eingabe == "h":
        while True:
            b = input("Was möchtest du hinzufügen? Falls beenden = b: ")
            if b in x:
                print("Fehler! in der Liste vorhanden ")
            elif b == "b":
                break
            else:
                x.append(b)
    elif eingabe == "e":
        while True:
            g = input("Möchtest du alles entfernen = a / Eine Sache = e / falls beenden = b: ")
            if g not in ["a", "e", "b"]:
                print("Fehler! Falsche Eingabe")
            elif g == "a":
                x.clear()
                print("alles gelöscht / wurde beendet!")
                break
            elif g == "e":
                while True:
                    z = input("Was möchtest du löschen? / falls zurück = z: ")
                    if z != "z" and z not in x:
                        print("Fehler! in der Liste nicht vorhanden / falsche Eingabe")
                        print(x)
                    elif z in x:
                        x.remove(z)
                        print(z, "wurde gelöscht")
                    else:
                        break
            else:
                break
    else:
        break
print("-----Programm beendet-----")
