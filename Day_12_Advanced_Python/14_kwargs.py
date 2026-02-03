def marks(**kwargs): # kwargs is dict. with all the key value pairs which were passed to marks
    for items in kwargs.keys():
        print(f"The result of {items} is {kwargs[items]} out of 100.")
    
marks(Tanzim = 54, Adil = 70, Aziz = 90)