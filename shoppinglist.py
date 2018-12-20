#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 23:46:03 2018

Shopping List with Python by Bashier Elfergani

@author: bashier2026
"""
#Updated Python Shopping List-User Interface
shopping_list = ["apples",]
shopping_list.insert(1,'orange')
shopping_list.insert(2,'cookies')
shopping_list.insert(3,'chips')
shopping_list.insert(4,'milk')
shopping_list.insert(5,'eggs')
shopping_list.insert(6,' ')


question = "Are you done?:no"

#Backend Program
name  =input('Enter your Name:   ')
print(f'Hello {name}, here is your Shopping List.\n This App is Currently in Beta')
print(".....")
for list in shopping_list:

 print(list)
done = input("Are you done with your list?:   ")
if done == "yes":
  print("Thank you for using our shopping list, Have a good day!")


elif done == "":
  print("Please answer the question")

else:
 print("Please keep adding to your shopping list..")
#End Program