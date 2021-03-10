import xlsxwriter  # Import tbe excel writer package


def executeExport(query):  # Create, close the workbook, create formats and calls the functions
    artist_info = query[0]  # Gets the artist info from the first index from getdate function(called in main)
    album_artist_name = artist_info[0] # Artist name
    print("[#2] Export Xlsx: Init export...")  # Print init showcase

    workbook = xlsxwriter.Workbook(str(album_artist_name) + '.xlsx')  # Create the xlsx file with the artist name
    bold = workbook.add_format({'bold': True})  # Create a format for the xlsx file
    blue = workbook.add_format({'color': 'blue'})  # Create a format for the xlsx file
    center = workbook.add_format({'align': 'center'})  # Create a format for the xlsx file
    __formatMusicWorksheet(workbook, bold, blue, query)  # Calls the function that format the songs worksheet
    __formatAlbumWorksheet(workbook, bold, blue, center, query)  # Calls the function that format the album worksheet
    workbook.close()  # Close and save the xlsx file


def __formatMusicWorksheet(workbook, bold, blue, query):  # Function that formats the music worksheet
    print("[#2] Export Xlsx: Init Music Worksheet format...")  # Print for showcase
    worksheet = workbook.add_worksheet("Musics")  # Add the music worksheet
    worksheet.set_column(0, 0, 80)  # Set the column size
    worksheet.set_column(1, 2, 15)  # Set the column size
    worksheet.write('A1', 'Song Name', bold)  # Set the A1 cell to "Song Name"
    worksheet.write('B1', 'Song Duration', bold)  # Set the B1 cell to "Song Duration"
    worksheet.write('C1', 'Song Rank', bold)  # Set the C1 cell to "Song Rank"

    songs_info = query[2]  # Gets the song infos that we need from the getdata function

    trackname_list, duration_list, rank_list, link_list = [[], [], [], []]  # Initialize variables
    for song in songs_info:  # For song in the song info array
        trackname_list.append(song[0])  # Append the song name to trackname_list
        duration_list.append(song[1])  # Append the duration to duration_list
        rank_list.append(song[2])  # Append the rank to the rank_list
        link_list.append(song[3])  # Append the link to link_list

    row = 1  # Initialize the row to 1 because of the row names
    col = 0  # Initialize the collum to 0
    for link in link_list:  # For to get all the links
        worksheet.write_url(row, col, link)  # Puts the links in the first collum in the row
        row +=1  # Add a row
    row = 1  # Reset the row
    col = 0  # Same collum so that the hyperlink stay in the name of the song
    for trackname in trackname_list:  # Puts the name over the link
        worksheet.write(row, col, trackname, blue)
        row +=1
    row = 1
    col = 1  # Change to the second collum
    for trackduration in duration_list:  # Gets the duration of the songs into the second collum
        worksheet.write(row, col, trackduration)
        row +=1
    row = 1
    col = 2  # Change to the third collum
    for trackrank in rank_list:  # Gets the rank of the song into the third collum
        worksheet.write(row, col, trackrank)
        row +=1
    print("[#2] Export Xlsx: finished Music format...")  # Print for showcase


def __formatAlbumWorksheet(workbook, bold, blue, center, query):  # Function that formats the album worksheet
    worksheet = workbook.add_worksheet('Albums')  # Add the albums worksheet
    worksheet.set_column(0, 0, 50)  # Set the column size
    worksheet.set_column(1, 4, 18)  # Set the column size
    worksheet.write('A1', 'Album Name', bold)  # Set the A1 cell to "Album Name"
    worksheet.write('B1', 'Album Duration', bold)  # Set the B1 cell to "Album Duration"
    worksheet.write('C1', 'Album Release Date', bold)  # Set the C1 cell to "Album Release Date"
    worksheet.write('D1', 'Album Fans', bold)  # Set the D1 cell to "Album Fans"
    print("[#2] Export Xlsx: Init Artist Worksheet format...")  # Print for showcase

    albuns_info = query[1]  # Gets the album infos that we need from the getdata function

    name_list, duration_list, fans_list, link_list, release_date_list = [[], [], [], [], []]  # Initialize variables
    for album in albuns_info:  # Same process as the song infos
        name_list.append(album[0])  # Append the album name to name_list
        duration_list.append(album[1])  # Append the duration to duration_list
        release_date_list.append(album[2])  # Append the release_date to release_date_list
        fans_list.append(album[3])  # Append the fans to fans_list
        link_list.append(album[4])  # Append the link to link_list

    row = 1
    col = 0
    for link in link_list:  # Same process as the song, so put the link and the name above so that the hyperlink stays
        worksheet.write_url(row, col, link)
        row +=1
    row = 1
    col = 0
    for name in name_list:  # Same process as the song
        worksheet.write(row, col, name, blue)
        row +=1
    row = 1
    col = 1
    for duration in duration_list:  # Same process as the song
        worksheet.write(row, col, duration)
        row +=1
    row = 1
    col = 2
    for release_date in release_date_list:  # Same process as the song
        worksheet.write(row, col, release_date, center)
        row +=1
    row = 1
    col = 3
    for fans in fans_list:  # Same process as the song
        worksheet.write(row, col, fans)
        row +=1
    print("[#2] Export Xlsx: finished Artist format...")  # Print for Showcase