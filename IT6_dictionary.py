dictionary_of_the_doctor ={
    1: "William Hartnell",
    2: "Patrick Troughton",
    3: "Jon Pertwee",
    4: "Tom Baker",
    5: "Peter Davison",
    6: "Colin Baker",
    7: "Sylvester McCoy",
    8: "Paul McGann",
    9: "Christopher Eccleston",
    10: "David Tennant",
    11: "Matt Smith",
    12: "Peter Capaldi",
    13: "Jodie Whittaker",
    14: "David Tennant",
    15: "Ncuti Gatwa"
}
# if you want to find out which actor played which incarnation of the Doctor, use the function below.

def which_actor(number):
    return dictionary_of_the_doctor[number]

print(which_actor(4))

# a dictionary is a collection of objects where every item has a reference key, allowing it to be found using that key. 
# this means the key can be connected information, rather than an otherwise unconnected index number, which can make it easier to find.
# similar to the list, this is a dictionary of most of the actors who played Dr Who
# a dictionary allows us to refer to the incarnation using the conventinal numbering
# insofar as it's possible to do so with Doctor Who. The function will pull out the actor's name
# based on the number of incarnation they played (the keys here being the numbers)
# this has been complicated slightly by returning actors.