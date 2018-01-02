from string import whitespace
import os
def is_sku(s):
    """ Returns True is string is a number. """
    skuLen = os.getenv("SKULEN") 
    s=s.replace(" ", "")
    print(s)
    if(len(s) >skuLen):
     try:
       float(s)
       print("returning valid sku")
       return True
     except ValueError:
       return False
    else:
      return False
