import re
def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]',password) is not None
    lowercase_criteria = re.search(r'[a-z]',password) is not None
    number_criteria = re.search(r'[0-9]',password) is not None
    specialchar_criteria = re.search(r'[\W_]',password) is not None

    strength=0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if specialchar_criteria:
        strength += 1

    feedback = "Password Strength : "
    if strength == 5:
        feedback += "Very Strong"
    elif strength == 4:
        feedback += "Strong"
    elif strength == 3:
        feedback += "Moderate"
    elif strength == 2:
        feedback += "Weak"
    else:
        feedback += "Very Weak"
    return feedback

def main():
    while True:
        password = input("Enter a password for strength assessment : ")
        feedback = assess_password_strength(password)
        print(feedback)
        if input("Do you want to assess another password? (yes/no) : ").lower()!='yes':
            break

if __name__ == "__main__":
    main()

