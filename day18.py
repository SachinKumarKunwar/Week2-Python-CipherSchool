## take two comma separated inputs from the user
# 1.) user's name , example - "Goswami"
# 2.) a single character  , "G"


## Output - 2 print lines
# 1.) user's name lines
# 2.) count the character that user inputed(bonus: case insensitive count) 


name,chr = input("enter comma seperated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"chr count : {name.count(chr)}") # case sensitive 

