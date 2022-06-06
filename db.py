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

# tulostetaan tietokannan collectioneiden nimet:
print(db.list_collection_names())