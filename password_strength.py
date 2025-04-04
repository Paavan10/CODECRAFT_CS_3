import re
import random
import string

def check_password_strength(password):
    strength_criteria = {
        "length (8 or 12 characters)": len(password) in [8, 12],
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"\d", password)),
        "special characters": bool(re.search(r"[@$!%*?&]", password))
    }
    
    strength_score = sum(strength_criteria.values())
    
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    if strength_score < 5:
        feedback = "Your password is not strong. It does not satisfy all conditions. "
        missing_criteria = [key for key, value in strength_criteria.items() if not value]
        feedback += "Consider adding: " + ", ".join(missing_criteria)
    else:
        feedback = "Your password meets all security criteria!"
        feedback += "\nTo make it even stronger, consider using a completely random passphrase. Example: "
        feedback += generate_strong_password_based_on_input(password)
    
    return strength, feedback

def generate_strong_password_based_on_input(password):
    additional_chars = string.ascii_letters + string.digits + string.punctuation
    enhanced_password = list(password)
    for _ in range(4):  # Adding four more random characters
        enhanced_password.append(random.choice(additional_chars))
    random.shuffle(enhanced_password)
    return ''.join(enhanced_password)

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    print(feedback)