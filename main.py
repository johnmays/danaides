from bs4 import BeautifulSoup
import json

def main():
    with open('./data/songs.json') as f:
        songs = json.load(f)
    
    count_all = len(songs)
    count_available = 0

    for song in songs:
        url = song['url']
        available = assess_availability(url)
        if available:
            # update json in memory
            count_available += 1

    # if changed, write json to file

def assess_availability(url:str) -> bool:
    """
    TO BE IMPLEMENTED
    """
    pass
    return True

if __name__ == '__main__':
    main()