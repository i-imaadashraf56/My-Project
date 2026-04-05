# My Introduction Project

print("👋 Hello! Welcome to my introduction program\n")

name = "Imaad Ashraf"
goal = "Preparing for Ausbildung in Germany"
interests = "Coding, Software Technology, Problem Solving"
fav_languages = "Python and JavaScript"

print("My Name:", name)
print("My Goal:", goal)
print("My Interests:", interests)
print("My Favorite Languages:", fav_languages)

print("\n--- Let's interact! ---\n")

# Asking user name
user_name = input("What's your name? ")

print("Nice to meet you,", user_name, "! 😊")

# Asking interest
user_interest = input("Do you like coding? (yes/no): ")

if user_interest.lower() == "yes":
    print("That's awesome! Coding is powerful 💻")
else:
    print("No worries! You can start learning anytime 🚀")

# Asking favorite language
fav = input("What's your favorite programming language? ")

print("Great choice!", fav, "is really cool! 😎")

print("\nThanks for visiting my introduction program!")