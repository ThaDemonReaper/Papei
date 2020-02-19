word=raw_input("give a word to try: ")
asciivalue=""
for char in word:
    asciivalue+=str(ord(char))
number=int(asciivalue)
def is_prime(number):
    if number % 2 == 0 or number % 3 == 0:
        print("is not prime")
    else:
        for i in range(5, int(number**0.5) + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                print("is not prime number")
                break
            else:
                print("is prime number")
                break

is_prime(number)