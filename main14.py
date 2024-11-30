def my_long_word(min_length, text):
        #initialiser une liste pour stocker les mots qui respectent la conditions
        long_word = []
        #decouper la chaine de texte en mots(par espace)
        word = ""

        for char in text:
                if char == " ":
                        if len(word) > min_length:
                                long_word.append(word)
                        word =""#reinitialiser le mot pour le prochain
                else:
                word += char
        
        
        if len(word) > min_length: 
                long_word.append(word)

        return " ".join(long_word)

text = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mère à la haine, la haine mère à la souffrance"
result = my_long_word(3, text)
print(result)

   
       
