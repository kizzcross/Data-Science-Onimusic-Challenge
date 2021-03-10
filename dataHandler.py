import requests  # Import Request Package
import utils  # Import Utils (package that removes duplicates from array)


def getdata(artist_id):  # Function that import the api and formats it

    print("[#1] Data: Getting data...")  # Print for showcase

    url = "https://api.deezer.com/artist/"+str(artist_id)  # Gets us the api with the id code provided in main.py

    artist_json = requests.get(url).json()  # Gets us the artist api and turn it into a readable format
    artist_info = [artist_json["name"], artist_json["link"]]  # Gets us the artist name and the artist link
    artist_album_count = artist_json["nb_album"]  # Gets us the number of artist albums

    url = "https://api.deezer.com/artist/"+str(artist_id)+"/albums"  # Gets the certain artist album api link

    artist_albuns_json = requests.get(url).json()  # Gets and turn the requested album api into a readable format
    artist_albuns_data = artist_albuns_json["data"]  # Receives the dicts array that contains the data

    while 'next' in artist_albuns_json:  # In the end of the api theres a next that gets the next page, so when there is no next, there is no pages left
        artist_albuns_json = requests.get(artist_albuns_json["next"]).json()  # Gets the next page api and turns it to a readable format
        artist_albuns_data += artist_albuns_json["data"]  # Receives the dicts array that contains the data
    albuns_id_array = __getArtistAlbunsIdArray(artist_albuns_data)  # Gets albums ids array
    albuns_library, songs_library = __getSongsOfAlbuns(albuns_id_array, artist_id)  # Gets the array that contains the songs and the albums information

    print("[#1] Data:",len(albuns_library),"/",artist_album_count,"albuns had been found.")  # Number of albums that we got by the number of albums that the artist has
    print("[#1] Data:",len(songs_library),"musics had been found.")  # Showcase how many musics we got
    
    return [artist_info, albuns_library, songs_library]  # Returns the artists info, album infos and songs infos


def __getArtistAlbunsIdArray(artist_albuns_data):  # Function that gets us the albums id array
    albuns_id_array = []  # Initializing the array

    for obj in artist_albuns_data:  # for objects in the artist array
        albuns_id_array.append(obj["id"])  # Gets us the id and include it into the array

    albuns_id_array = utils.get_unique_numbers(albuns_id_array)  # removes the repeated id's
    return albuns_id_array  # Returns the albums id array without repetitions


def __getSongsOfAlbuns(albuns_id_array, artist_id):  # Function that gets the albuns and songs info array
    # albuns_library = album_info
    # songs_library = songs_info
    # albuns_library = [title,duration,release_date,fans,link] (order of the vectors)
    # songs_library = [name,duration,rank,link] (order of the vectors)

    albuns_library = []  # Initializing the array
    songs_library = []  # Initializing the array

    for album_id in albuns_id_array:  # For every id's that is not repeated
        url = "https://api.deezer.com/album/"+str(album_id)  # Get the album id url
        album_json = requests.get(url).json()  # Gets and turn the requested album api into a readable format

        album_info = [album_json["title"],album_json["duration"],album_json["release_date"],album_json["fans"],album_json["link"]]
        albuns_library.append(album_info)  # Append the desired information of the album

        tracks = album_json["tracks"]  # Gets the album tracks

        for song in tracks["data"]:  # For every song in tracks data
            song_artist_temp = song["artist"]  # Gets a temporary artist info
            if int(song_artist_temp["id"]) == artist_id:  # Checks if the id of the song is the same as the artist so wrong artists wont be added
                song_info = [song["title"],song["duration"],song["rank"],song["link"]]  # Gets the song info that we need
                songs_library.append(song_info)  # Append the song info to an array

    return albuns_library, songs_library  # Export the desired album info and song info