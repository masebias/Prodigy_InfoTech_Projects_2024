def check_password_strength(password):
    strength_level = "Weak"
    suggestions = []

    # Check if the password is at least 8 characters long
    if len(password) < 8:
        suggestions.append("The password should be at least 8 characters long")
    else:
        # Check if the password contains at least one uppercase letter
        if not any(c.isupper() for c in password):
            suggestions.append("The password should contain at least one uppercase letter")
        # Check if the password contains at least one lowercase letter
        if not any(c.islower() for c in password):
            suggestions.append("The password should contain at least one lowercase letter")
        # Check if the password contains at least one digit
        if not any(c.isdigit() for c in password):
            suggestions.append("The password should contain at least one digit")
        # Check if the password contains at least one special character
        if not any(c in '!@#$%^&*(),.?":{}|<>' for c in password):
            suggestions.append("The password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")

        # Determine the strength level
        if len(suggestions) == 0:
            strength_level = "Strong"
        elif len(suggestions) < 3:
            strength_level = "Moderate"
        else:
            strength_level = "Weak"

    return strength_level, suggestions


password = input("Please input a password: ")
strength, suggestions = check_password_strength(password)
print(f"Strength: {strength}")
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
