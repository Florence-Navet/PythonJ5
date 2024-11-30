def my_long_word(min_length, text):
    # Initialiser une liste pour stocker les mots qui respectent la condition
    long_word = []
    
    # Découper la chaîne de texte en mots (par espace)
    word = ""

    for char in text:
        if char == " ":
            if len(word) > min_length:
                long_word.append(word)
            word = ""  # Réinitialiser le mot pour le prochain
        else:
            word += char  # Ajouter le caractère au mot en cours

    # Ajouter le dernier mot si nécessaire
    if len(word) > min_length: 
        long_word.append(word)

    # Retourner la liste des mots plus longs que la longueur spécifiée
    return " ".join(long_word)

# Exemple d'utilisation
text = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
result = my_long_word(3, text)
print(result)
