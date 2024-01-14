'''Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.'''
countries_and_capitals = {
            "Nepal" : "Kathmandu",
            "UK" : "London",
            "France" : "",
            "Poland" : "Warsaw",
            "Germany" : "",
            "Hungary" : "Budapest"}

while True:
    country = input("Enter a country: ")

    found = False

    for i in countries_and_capitals:
        
        if i.lower() == country.lower():
            
            found = True
            
            if countries_and_capitals[i] == "":
                capital = input("Enter capital: ")
                
            else:
                print(countries_and_capitals[i])

    if found == False:
        print("Country not found")
    
    cont = input("Continue?(y/n) ").lower()
    
    if cont == "n" or cont == "no":
        break
    
    else:
        continue
    


    
