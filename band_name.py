'''This code generates a band name based on the user's input of their city 
and pet's name.It prompts the user for their city and pet's name, 
then combines them to create a unique band name. The result is printed to the console.
This is a simple and fun way to create a band name that is personal to the user 
and can be used for various creative purposes.'''

print("Welcome to the Band Name Generator!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's the name of your pet?\n")
band_name = city + " " + pet
print("Your band name could be: " + band_name)
