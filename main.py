# In Terminal, Command Prompt: pip install pymongo
# In Terminal, Command Prompt: pip install "pymango[srv]"
import pymongo
client = pymongo.MongoClient("mongodb+srv://rahulthavai1991:Jeevika2021@cluster0.x1inj5y.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name": "rahul",
    "email": "rahulthavai1991@gmail.com",
    "surname": "Thavai"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)