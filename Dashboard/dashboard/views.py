import json

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import pymongo

import requests



def dash(request):
   return render(request,'dashboard.html')

# mongodb connection

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Netclan"]


mycollection = db["Netfile"]



one_record = mycollection.find_one()



print(one_record)



all_records = mycollection.find()

list_all = list(all_records)
# print(list_all)




