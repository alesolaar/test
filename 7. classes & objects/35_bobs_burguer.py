class restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = True

bobs_burguer = restaurant()
bobs_burguer.name = 'Bob\'s Burgers'
bobs_burguer.category = 'American Diner'
bobs_burguer.rating = 4.7
bobs_burguer.delivery = False

print(vars(bobs_burguer))