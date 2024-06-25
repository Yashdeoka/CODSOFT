import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Invalid input. Length must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        password = generate_password(length)
        print(f"Generated password: {password}")
        
        repeat = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
