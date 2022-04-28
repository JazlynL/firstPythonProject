STUDENTS = ["Becky", "Jake", "Cameron", "Jessie", "Karol", "Frankie"]
SCHOOL_NAME = "Career Devs"

# challenge 1
# accept = input("Hello are you a student at " + SCHOOL_NAME + "? \n (yes/no)")
# if accept == "yes":
#     name = input("Okay What is your Name ? \n Name:")
#     for stu_name in STUDENTS:
#         if name == stu_name:
#             print("Welcome to class")
#
#             break
#
#
# else:
#     print("You are not supposed to be here.")


# Bonus challenges
# Ignore the whitespace of the user inputs
# allow all inputs that start with ‘y’ to be a valid ‘yes’
# allow a user to re-enter if they don't enter yes or no

# accept = input("Hello are you a student at " + SCHOOL_NAME + "? \n (yes/no)").strip()
# if accept[0] == "y":
#     name = input("Okay What is your Name ? \n Name:")
#     for stu_name in STUDENTS:
#         if name == stu_name:
#             print("Welcome to class")
#
#             break
#
# else:
#     print("You are not supposed to be here.")

accept = " "
while accept == "" or accept[0] != "y" and accept[0] != "n":
    accept = input("Hello are you a student at " + SCHOOL_NAME + "? \n (yes/no)").strip()
if accept[0] == "y":
    name = input("Okay What is your Name ? \n Name:")
    for stu_name in STUDENTS:
        if name.casefold() == stu_name.casefold():
            print("Welcome to class")

            break

else:
    print("You are not supposed to be here.")
