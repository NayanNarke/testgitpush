import pymongo

client = pymongo.MongoClient("mongodb+srv://nay_mongoDB:nayan_027@naycluster.ymwu6ax.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "nayan",
    "surname" : "narke",
    "email" : "nayan123@gmail.com"
}

db1 = client['mongodbtest']
coll = db1['test']
coll.insert_one(d)