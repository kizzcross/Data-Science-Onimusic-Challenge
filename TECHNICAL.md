# Technical Explananation

## Classes/Script Files
- ``DataHandler.py``: contain the functions that get and filter the Data, such as the musics and the albuns
- ``utils.py``: has the function that remove the repeted numbers from an array, and its used to remove the repeted albuns id's so that we didnt export repeted albuns.
- ``exportExcel.py``: contain the function that formats and export the excel file

## My problems/difficulties
- The deezer Api by default returns only the top 100 songs by an artist, so to get all the musics I had to get all the musics from the album that the music was, then filter if the artist was or wasn't in the song, and to get that part to work was a bit difficult.

## Contribuitors

Thank to all contribuitors:
<table>
    <td align="center"><a href="https://github.com/Rastrian"><img src="https://avatars.githubusercontent.com/u/68169692?s=460&u=18d8c83d147b111b2aa87dc8ae228500b3105d85&v=4" width="100px;" alt="Joao Victor (kizzcross)"/><br /><sub><b>Joao Victor (kizzcross)</b></sub></a></td>
</table>

## Images
<img src="https://github.com/kizzcross/Data-Science-Onimusic-Challenge/blob/master/assets/1.png?raw=true"  />
<img src="https://github.com/kizzcross/Data-Science-Onimusic-Challenge/blob/master/assets/2.png?raw=true"  />
