'''Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].'''

def sorter(s):
    new_list = []
    for i in s:
        new_list.append(i)
    new_list.sort()
    
    new_list = set(new_list)
    
    new_list = list(new_list)
    
    new_list.sort()
        
    return new_list

x = input("Enter a string: ")
y = sorter(x)
print(y)
