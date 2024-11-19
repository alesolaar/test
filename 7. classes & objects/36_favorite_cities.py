class city:
    def __init__(self, name='', country='', population=0, landmarks=['']):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

valladolid = city('Valladolid', 'Spain', 500000, ['Plaza Zorrilla'])

print(vars(valladolid))
