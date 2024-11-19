import random
from functools import reduce

# Prefijos y sufijos
prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

# Función para generar nombres
def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

# Capitalizar los sufijos
def capitalize_suffix(suffix):
    return suffix.capitalize()

capitalized_suffixes = list(map(capitalize_suffix, suffixes))

# Generar 10 nombres fantásticos
random_names = [create_fantasy_name(prefixes, capitalized_suffixes) for _ in range(10)]

# Función para verificar si 'Fire' está en el nombre
def fire_in_name(name):
    return 'Fire' in name

# Función para concatenar nombres
def concatenate_names(name1, name2):
    return name1 + ' ' + name2

# Filtrar nombres con 'Fire'
filtered_names = list(filter(fire_in_name, random_names))

# Reducir nombres filtrados
reduced_name = reduce(concatenate_names, filtered_names) if filtered_names else "No names with 'Fire'"

# Mostrar información
def display_name_info(random_names, filtered_names, reduced_name):
    print("Generated Fantasy Names:")
    for name in random_names:
        print(name)
    print("\nFiltered Names with 'Fire':")
    for name in filtered_names:
        print(name)
    print("\nReduced Name:")
    print(reduced_name)

# Llamar a la función para mostrar los resultados
display_name_info(random_names, filtered_names, reduced_name)
