This project demonstrates a simple hospital login system prototype emphasizing authentication logic and access control.

The objective is to illustrate basic security reasoning in authentication systems, including credential validation and controlled access.

This project is intended for academic illustration only and does not use real hospital data.

# Password Strength Checker
# Academic illustration only

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()" for c in password):
        score += 1

    return score

def main():
    password = input("Enter a password to check strength: ")
    score = check_strength(password)

    if score <= 2:
        print("Weak password")
    elif score == 3:
        print("Moderate password")
    else:
        print("Strong password")

if __name__ == "__main__":
    main()
