# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:13:23 2021

@author: issac
"""

import sqlite3


test_password="123456"

print("Welcome to Password Manager")


limit =0

while limit!=5:
    connection=input("What is your password? \n")
   
    if connection==test_password:
        print("Right")
        break
        
    else:
        limit+=1
        print("Wrong")
        print("You have ", 5-limit," attempts left")



conn=sqlite3.connect('password.db')
print ("Opened database successfully")

print("\n"+"*"*15)
print("Commands:")
print("q = quit program")
print("get = get password")
print("store = store password")
print("*"*15)

conn.close()
