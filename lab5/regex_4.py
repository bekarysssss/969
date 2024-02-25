import re

def find_sequences(text):
    formul = r'[A-Z][a-z]+'
    R = re.findall(formul, text)
    return R
       
best_song_lyrics = "Never Was much Of a romantic, I Could Never Take the Intimacy"
sequences = find_sequences(best_song_lyrics)
print("Uppercase words:")
print(sequences)