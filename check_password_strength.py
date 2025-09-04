import re
import math

def calculate_entropy(password):
    """Calculate password entropy based on character set size"""
    char_set = 0
    if re.search(r"[a-z]", password):
        char_set += 26
    if re.search(r"[A-Z]", password):
        char_set += 26
    if re.search(r"[0-9]", password):
        char_set += 10
    if re.search(r"[a-zA-Z0-9]", password):
        char_set += 32
    if char_set == 0:
        return 0
    entropy = len(password) * math.log2(char_set)
    return entropy

def check_password_strength(password):
    """Evaluate password strength and return feedback"""
    score = 0
    feedback = []

    # check length
    if len(password) >= 8 :
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long")

    # check character variety
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add updercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # check against common password
    common_passwords = ["password", "123456", "qwerty"]

    if password.lower() in common_passwords:
        score = 0
        feedback.append("This is a common password: choose something unique.")

    entropy = calculate_entropy(password)
    if entropy < 50:
        feedback.append("Low entropy: consider a longer or more varied password.")

    if score >= 5 and entropy >= 50:
        strength =  "Strong"
    elif score >=3:
        strength = "Medium"
    else:
        strength = "week"

    return strength, feedback

def main():
    password = input("Enter a password to analyze: ")
    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    print(f"Entropy: {calculate_entropy(password):.2f} bits")

if __name__ == "__main__":
    main()