
# Create a playlist of liked songs

# Output should be:
# Liked Songs:
# Bad Habits by Ed Sheeran
# I'm Just Ken by Ryan Gosling
# Mastermind by Taylor Swift
# Uptown Funk by Mark Ronson ft. Bruno Mars
# Ghost by Justin Bieber

# Dictionary of liked songs
liked_songs = {
  'Whats Going On': 'Marvin Gaye',
  'Woman of the World': 'Marvin Gaye',
  'What Are You Doing For The Rest of Your Life': 'Bill Evans',
  'Water No Get Enemy': 'Fela Kuti'
}


# Function to write the liked songs to a file
def write_liked_songs_to_file(liked_songs, file_name):
    file = open(file_name, 'w')
    file.write('Liked Songs:\n')

    for key, value in liked_songs.items():    
        file.write(f'{key} by {value}\n')

    file.close()
# Writing the songs to a file

filename = '07-FileHandling.txt'

write_liked_songs_to_file(liked_songs, filename)


