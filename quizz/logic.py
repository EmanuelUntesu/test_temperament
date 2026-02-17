# quizz/logic.py

# TABEL NR. 1: Cheia de răspunsuri (True = DA, False = NU)
CHEIE_RASPUNSURI = {
    'flegmatic': {
        2: True, 25: False, 26: True, 27: True, 29: True, 30: True, 
        34: True, 42: False, 43: False, 49: True, 50: True, 51: True, 
        55: True, 56: False, 65: True, 67: True, 69: True, 75: True, 78: True
    },
    'coleric': {
        1: True, 3: True, 6: True, 8: False, 10: False, 11: True, 
        18: True, 23: True, 32: True, 38: False, 45: True, 47: True, 
        52: True, 53: True, 54: True, 60: True, 68: True, 74: True, 76: True, 80: False
    },
    'sangvin': {
        5: False, 7: False, 9: False, 12: False, 16: True, 19: False, 
        20: True, 22: True, 35: True, 36: True, 39: True, 40: False, 
        41: True, 48: True, 57: True, 59: True, 60: True, 61: True, 
        62: True, 63: True, 70: True, 71: True, 72: True
    },
    'melancolic': {
        4: True, 13: True, 14: True, 15: True, 17: True, 19: True, 
        21: True, 24: True, 25: True, 28: True, 31: True, 33: True, 
        34: False, 37: True, 42: True, 43: True, 44: True, 46: True, 
        56: True, 58: True, 64: True, 66: True, 73: True, 77: True
    }
}

# TABEL NR. 2: Conversia Punctaj Brut -> Procentaj
CONVERSIE_PROCENTE = {
    'flegmatic': {
        0: 0, 1: 1, 2: 3, 3: 6, 4: 9, 5: 13, 6: 14, 7: 23, 8: 28, 9: 33, 
        10: 38, 11: 43, 12: 49, 13: 55, 14: 61, 15: 68, 16: 74, 17: 81, 18: 88, 19: 94, 20: 98
    },
    'coleric': {
        0: 0, 1: 0.3, 2: 0.5, 3: 1, 4: 2, 5: 4, 6: 5, 7: 8, 8: 11, 9: 14, 
        10: 18, 11: 24, 12: 29, 13: 35, 14: 41, 15: 48, 16: 56, 17: 65, 18: 74, 19: 83, 20: 91, 21: 97
    },
    'sangvin': {
        0: 0, 1: 1, 2: 3, 3: 5, 4: 7, 5: 9, 6: 12, 7: 16, 8: 19, 9: 23, 
        10: 27, 11: 32, 12: 37, 13: 42, 14: 47, 15: 52, 16: 58, 17: 63, 18: 70, 19: 76, 20: 82, 21: 89, 22: 94, 23: 97, 24: 99
    },
    'melancolic': {
        0: 0, 1: 1, 2: 4, 3: 5, 4: 12, 5: 17, 6: 18, 7: 22, 8: 28, 9: 33, 
        10: 38, 11: 44, 12: 49, 13: 54, 14: 59, 15: 64, 16: 69, 17: 74, 18: 78, 19: 82, 20: 86, 21: 90, 22: 93, 23: 96, 24: 98, 25: 99
    }
}

def calculeaza_rezultate(raspunsuri_utilizator):
    """
    raspunsuri_utilizator: dicționar de forma {id_intrebare: True/False}
    """
    scoruri_brute = {'flegmatic': 0, 'coleric': 0, 'sangvin': 0, 'melancolic': 0}

    # 1. Calculăm punctajul brut bazat pe Tabelul 1
    for temperament, cheie in CHEIE_RASPUNSURI.items():
        for nr_intrebare, raspuns_corect in cheie.items():
            # Verificăm dacă utilizatorul a răspuns la întrebare
            # și dacă răspunsul coincide cu cel din tabel
            if raspunsuri_utilizator.get(nr_intrebare) == raspuns_corect:
                scoruri_brute[temperament] += 1

    # 2. Convertim punctajul brut în procente conform Tabelului 2
    rezultate_finale = {}
    for temperament, punctaj in scoruri_brute.items():
        tabel_conversie = CONVERSIE_PROCENTE[temperament]
        # Luăm procentul, iar dacă punctajul e cumva peste maxim (eroare), luăm valoarea maximă disponibilă
        rezultate_finale[temperament] = tabel_conversie.get(punctaj, max(tabel_conversie.values()))

    return rezultate_finale