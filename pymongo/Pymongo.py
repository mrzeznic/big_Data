# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:26:08 2018

@author: <user>
"""

import pymongo

# help(pymongo.MongoClient)
client = pymongo.MongoClient(host='localhost', port=27017)

print(client.list_database_names())

b_data = client['company']['males']


def count_words(dic):
    x = len(dic['position'].split('_'))
    y = len(dic['favorite_book'].split(' '))
    z = x + y
    return z
for b in b_data.find():
    b_data.update_one({'_id': b['_id']}, {"$set": {'word_count': count_words(b)}})

print(b_data.find_one())
# client.close()
