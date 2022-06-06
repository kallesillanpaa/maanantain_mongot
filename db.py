from pymongo import MongoClient
import passw
password = passw.PASSWORD
connection_string = "mongodb+srv://kalle:"+password+"@cluster0.fnmyz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

#db = client['AlbumDB'] #tämä toimii myös
db = client.AlbumDB #luo autom. jos ei ole
albums = db.Albums  #luo autom.jos ei ole
                    #mutta näyttää ne vasta
                    # kun siellä on dataa



def add_album(artist,album,year,genre):
#     #ei palauta mitään, 
#     # vaan insert_one()-metodilla 
#     # lisätään parametreina tulleet arvot 
#     # albums-collectioniin
#     #->katso mallia W3-Insert -kohdasta
    albums.insert_one( {
        'artist':artist,
        'album':album,
        'year':year,
        'genre':genre
    })

def fetch_albums():
    result = []
    for row in albums.find():
        result.append(
            row['artist'] +
            " - " +
            row['album'] + 
            " - " + 
            str(row['year']) + #int muutetaan>string
            " - " +
            row['genre']      
            )        
     
    return result
    #käy find()-metodilla läpi for-loopilla
    #rivi riviltä tulokset, ja palauta
    #(returnilla) tulokset.
    #luo tyhjä lista, ja rivi riviltä lisää
    #listaan rivin tiedot append-metodilla.
    
    #Haluttu result on muodossa:
    #Deep Purple-Fireball-1970-Rock 

# --------------------------------------------------

# tulostetaan tietokannan collectioneiden nimet:
# print(db.list_collection_names())

# # kaikkien tietueiden haku:
# for row in albums.find():
#     print(row['artist'],row['album']) 
# #     #joka rivin artist-keyn value

# #yhden tietueen haku:
# res = albums.find_one()
# print(res)

# #haku tietyn kentän mukaan:
# res = albums.find_one({'album':'Fireball'})
# print(res)

