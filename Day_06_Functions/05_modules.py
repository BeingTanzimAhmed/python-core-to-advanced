'''
Two types of modules in python : 
1. Built-in Modules 
2. External Modules

Python built-in modules index: https://docs.python.org/3/py-modindex.html
'''

import math #Example of built-in modules
import mymodule
import requests

print(math.sqrt(4))
print(mymodule.greet("Amman"))
r = requests.get("https://www.google.com") # This function can always be used to get the html of any website

print(r.text)