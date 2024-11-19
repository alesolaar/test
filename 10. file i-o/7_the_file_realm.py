liked_songs={
'Labyrinth': 'Taylor Swift',
'Blue Celeste':'Blanco',
'Notti in Bianco':'Blanco',
'Little Things':'One Direction',
}

def write_liked_songs_to_file(liked_songs, songs):
    with open('songs.txt', 'w') as file:
        file.write('liked songs:\n')
        for song,artist in liked_songs.items():
            file.write(f'{song} by {artist}\n')
    
write_liked_songs_to_file(liked_songs, 'songs.txt')