doctors = ["hartnell",
            "troughton",
            "pertwee", 
            "t_baker", 
            "davison", 
            "c_baker", 
            "mccoy", 
            "mcgann",
            "eccleston"
            "tennant",
            "smith",
            "capaldi",
            "whittaker",
            "gatwa"]

def doctor_actor(int):
    return(doctors)[int]
# for int please select a number between 0-13
print(doctor_actor(3))

# a list is an indexed group of related items.
# they know where items are in the list, that's it. 
# this list is of the actors who have played Dr Who (give or take)
# the function requires you to add an integer between 0 and 13 to 
# retrieve an actor's name. However it is a bit unsatisfying as you 
# have to enter a number one lower than the numbering used in the show
# in order to retrieve a name (eg Tom Baker = 3). this is because the index
# reference numbers start at 0