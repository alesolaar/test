def get_item(x):
    if x == 1:
        return '🍔 Cheeseburger'

    if x == 2:
        return '🍟 Fries'
    
    if x == 3:
        return '🥤 Soda'
    
    if x == 4:
        return '🍦 Ice Cream'
    
    if x == 5:
        return '🍪 Cookie'
    

def welcome():
    option = int(input("¿Qué quieres comer?: "))
    print(get_item(option))

welcome()