# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:00:27 2018

@author: <user>
"""
from json.objectid import ObjectId
import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://<user>:<pswd>@mycluster-ly5yx.mongodb.net/test?retryWrites=true")

db = client.database_names()

data_base = client.company.workers
data_base_1 = client['company']['workers']
my_find = data_base.find_one({'_id': '<id>'})
print(my_find)
# print(data_base.collection_names())
# print(data_base_1.collection_names())

