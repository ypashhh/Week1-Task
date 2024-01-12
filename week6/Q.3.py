'''Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"The {num} is not prime number.")
            break
    else:
        print(f"The {num} is prime number.")


if __name__ == "__main__":
    try:
        num= int(input("Enter a number: "))
        if num < 2:
            print(f"{num} is not a prime number")

        else:
            is_prime(num)

    except ValueError:
        print("Invalid input")