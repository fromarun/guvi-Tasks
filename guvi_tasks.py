# -*- coding: utf-8 -*-
"""guvi tasks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10eB3FTAxclnVC_xGz6JWNImoUHVJWOpo
"""



!pip install dnspython
!pip install pymongo[srv]
import pymongo
client = pymongo.MongoClient("mongodb+srv://arunkumar:1234@cluster0.kvcpn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.mong
records=db.mongcolle
for i in range(1,4):
    name = ""
    mobile = 0
    emailid = ""

    n = input("Enter your name :")
    cap = n.capitalize()
    name = cap

    while True:
        m = input("Enter your mobile number: ")
        if m.isdigit() and len(m) == 10:
            mobile = m
            break
        else:
            print("please enter a correct mobile number")
            continue

    while True:
        u = input("  Enter your email id ")
        x = list(map(str, u))
        if "@" in x and "." in x and x[0].isalpha():
            y = u.split("@")
            z = list(map(str, y[1]))
            l = y[1].split(".")
            if l[0].isalpha() or l[0].isalnum():
                emailid = u
                break
            else:
                print("-------Enter a your email id correctly------ ")

        else:
            print("-------Enter a your email id correctly------ ")
            continue
    dict = {"_id": 0,
            "names": "",
            "mobiles": "",
            "emailids": ""}
    dict["_id"] = i
    dict["names"] = name
    dict["mobiles"] = mobile
    dict["emailids"] = emailid
    records.insert_one(dict)
    print("Successfully saved in the database ")