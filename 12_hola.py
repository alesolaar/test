def translator(language):
    # Diccionario de traducciones
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    # Función interna para traducir palabras
    def translate_word(word):
        if word in translations[language]:
            return translations[language][word]  # Devuelve la traducción si existe
        else:
            return "Translation not found"  # Mensaje si no encuentra la traducción

    return translate_word  # Devuelve la función interna



# Crear un traductor al español
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))  # Salida: hola
print(translate_to_spanish('goodbye'))  # Salida: adiós
print(translate_to_spanish('please'))  # Salida: Translation not found

# Crear un traductor al francés
translate_to_french = translator('french')
print(translate_to_french('hello'))  # Salida: bonjour
print(translate_to_french('thank you'))  # Salida: merci

# Crear un traductor al italiano
translate_to_italian = translator('italian')
print(translate_to_italian('hello'))  # Salida: ciao
print(translate_to_italian('goodbye'))  # Salida: arrivederci
