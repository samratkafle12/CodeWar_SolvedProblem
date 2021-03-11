import re

def song_decoder(song):
    # song = re.sub(r'(WUB)+'," ",song)
    # song = song.strip()
    # return song
    return " ".join(song.replace('WUB', ' ').split())

song ="WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUB"

print (song_decoder(song))