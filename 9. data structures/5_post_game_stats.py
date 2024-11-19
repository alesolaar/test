
# Lista de jugadores
players = [
    {'name': 'John Smith', 'position': 'Quarterback', 'jersey number': 12, 'yards': 350, 'touchdowns': 4},
    {'name': 'Mike Johnson', 'position': 'Wide Receiver', 'jersey number': 88, 'yards': 120, 'touchdowns': 2},
    {'name': 'Chris Lee', 'position': 'Running Back', 'jersey number': 33, 'yards': 200, 'touchdowns': 1},
    {'name': 'Tom Brown', 'position': 'Linebacker', 'jersey number': 54, 'yards': 0, 'touchdowns': 0},
]


positions= [player['position'] for player in players]
print('Player Positions:', positions)

for player in players:
    if player['name'] == 'John Smith':
        player['yards'] += 50
        player['touchdowns'] +=2

total_yards=sum(player['yards'] for player in players)
total_touch=sum(player['touchdowns'] for player in players)
num_players= len(players)

media_yards=total_yards/num_players
media_touch=total_touch/num_players

print(f'Average yards: {media_yards}')
print(f'Average yards: {media_touch}')
