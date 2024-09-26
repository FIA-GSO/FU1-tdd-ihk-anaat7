
def berechne_prozentwert(erreichte_punkte, max_punkte):
    if not isinstance(erreichte_punkte, (int, float)) or not isinstance(max_punkte, (int, float)):
        raise TypeError("Erreichte Punkte und maximale Punkte müssen Zahlen sein.")
    if erreichte_punkte < 0 or max_punkte < 0:
        raise ValueError("Erreichte Punkte und maximale Punkte dürfen nicht negativ sein.")
    if max_punkte == 0:
        raise ValueError("Maximale Punktezahl darf nicht 0 sein.")
    return (erreichte_punkte / max_punkte) * 100


def berechne_note(prozentwert):

    if not isinstance(prozentwert, (int, float)):
        raise TypeError("Der Prozentwert muss eine Zahl sein.")
    try:
        prozentwert = float(prozentwert)
        
        if 92 <= prozentwert <= 100:
            return "sehr gut"
        elif 81 <= prozentwert < 92:
            return "gut"
        elif 67 <= prozentwert < 81:
            return "befriedigend"
        elif 50 <= prozentwert < 67:
            return "ausreichend"
        elif 30 <= prozentwert < 50:
            return "mangelhaft"
        else:
            return "ungenügend"
    
    except ValueError:
        raise ValueError("Der Prozentwert muss eine gültige Zahl sein.")
