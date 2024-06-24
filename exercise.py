# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    
    letter = input("Enter a letter:").lower()

    if len(letter) > 1:
        print("Enter a single letter")
        return
    
    if not letter.isalpha():
        print("Enter a letter from a-z")
        return
    
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


# Call the function
check_letter()

##-----------------------------------------------------------------------------------------##

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    inputage = input("Please enter your age: ")

    age = int(inputage)

    if age < 1:
        print("Enter a valid age")
        return

    votingage = 18

    if age < 18:
        print("You are not eligible to vote")
    else:
        print("You are eligible to vote")

# Call the function
check_voting_eligibility()

##-----------------------------------------------------------------------------------------##

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here

    inputage = input("Input a dog's age: ")

    dogage = int(inputage)

    if dogage < 1:
        print("Enter a valid age")
        return

    if dogage < 3:
        realage = dogage*10
        print(f"The dog's age in dog years is {realage}.")
    else:
        realage = 20 + (dogage-2)*7
        print(f"The dog's age in dog years is {realage}.")

# Call the function
calculate_dog_years()

##-----------------------------------------------------------------------------------------##

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    iscold = input("Is it cold? (yes/no): ").lower()
    
    if iscold != "yes" or iscold != "no"
        print("Please enter 'yes' or 'no'.")
        return
    
    israining = input("Is it raining? (yes/no): ").lower()

     if israining != "yes" or iscold != "no"
        print("Please enter 'yes' or 'no'.")
        return

    if iscold == 'no' and israining == 'no':
        print("Wear light clothing.")
    elif iscold == 'yes' and israining == 'yes':
        print("Wear a waterproof coat.")
    elif iscold == 'yes' and israining == 'no':
        print("Wear a warm coat.")
    elif iscold == 'no' and israining == 'yes':
        print("Carry an umbrella.")

# Call the function
weather_advice()

##-----------------------------------------------------------------------------------------##

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here

     month = input("Enter the month of the year (Jan - Dec):")

     if month not in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        print("Please enter a valid month.")
        return

    day = int(input("Enter the day of the month:")

    if day < 1 or day > 31:
        print("Please enter a day between 1 and 31.")
        return
    
    if (month == "Dec" and day >= 21) or month == "Jan" or month == "Feb" or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month == "Apr" or month == "May" or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month =="Jul" or month == "Aug" or (month == "Sep" and day <= 21):
        season = "Summer"
    else (month == "Sep" and day >= 22) or month == "Oct" or month == "Nov" or (month == "Dec" and day <= 20):
        season = "Fall"

    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()