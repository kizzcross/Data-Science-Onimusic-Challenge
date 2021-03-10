from dataHandler import getdata  # Import function that gets the data from the api
from exportExcel import executeExport  # Import the function that exports the xlsx file

# data[] -> (data.[].album.id + c) -> (a + b) -> total
artist_id = 4538892  # Artist id CHANGE IF DESIRED
query = getdata(artist_id)  # Execute the getdate function and store the info to query
executeExport(query)  # Execute the function that export the xlsx file with the query parameter
