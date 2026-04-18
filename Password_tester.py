import re   

def check_password(password):
    score = 0

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    # Character checks
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Final strength
    if score >= 6:
        return "Strong"
    elif score >= 3:
        return "Average"
    else:
        return "Weak"

if __name__ == "__main__":
    password = input("Enter a password: ")
    strength = check_password(password)
    print(f"\nPassword Strength: {strength}")
