from function_variables.faces import convert

def test_faces():
    # Add your test cases here
    result = convert("Hello :) Goodbye :(")
    assert "Hello 🙂 Goodbye 🙁" == result



# Example 1: Simple binary selection (if-else)
temperature = 25
if temperature > 30:
    print("It's hot today! Remember to stay hydrated.")
else:
    print("The temperature is pleasant today.")


score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")


day = input("What day is it?")

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday":
        print("It's the start of the work week.")
    case "Friday":
        print("It's almost the weekend!")
    case _:
        print("It's a regular weekday.")

day = input("What day is it?")
is_holiday = input("Is it a holiday? (yes/no)")
has_class = input("Do you have class? (yes/no)")

if is_holiday == "yes":
    print("No school today!")
else:
    if day == "Saturday" or day == "Sunday":
        print("It's the weekend!")
    else:
        if has_class == "yes":
            print("You have class today.")
        else:
            print("No class today, but it's a school day.")


import random
# Get the secret number from random
secret_number = random.randint(1, 10)

attempts = 0
while True:
    # Ask the user for their guess
    user_guess = int(input("Guess a number between 1 and 10: "))

    attempts += 1
    
    if user_guess < secret_number:
        print("Too low!")
    elif user_guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the correct number in {attempts} attempt(s).")
        break


# Sample student grades list
student_grades = [87, 92, 76, 65, 95, 88, 72, 90, 84, 79]
    
total = 0
for grade in student_grades:
    total += grade

average = total / len(student_grades)
print(f"The average grade is: {average:.2f}")

total = 0 
index = 0
while index < len(student_grades):
    total += student_grades[index]
    index += 1
    
average = total / len(student_grades)
print(f"The average grade is: {average:.2f}")




