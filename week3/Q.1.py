'''Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before.'''

greeting = input("Hello! What is you name: ")

if greeting == "":
    print("Hello, Stranger!")

else:
    print(f"Hello! {greeting}. How are you?")


