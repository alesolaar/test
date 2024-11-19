from functools import reduce
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
    return song[1] > 5.0

longer_songs = list(filter(longer_than_five_minutes,playlist))


def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration - minutes)*100
    total_seconds = minutes * 60 + round(seconds)
    return total_seconds

seconds_song = list(map(minutes_to_seconds,playlist))

def add_durations(total, duration_in_seconds):
    return total + duration_in_seconds

total_duration = reduce(add_durations, seconds_song, 0)


print(longer_songs)
print(seconds_song)
print(total_duration)
