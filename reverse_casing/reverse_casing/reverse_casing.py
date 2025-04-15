full_name = input("Please enter your full name (in incorrect casing):")

full_name = ''.join(char.lower() if char.isupper() else char.upper() for char in full_name)

print(full_name)
