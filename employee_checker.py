COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the " + COMPANY_NAME + " employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- " + emp_name)
print("\n")

# user input section (buggy code)



# input from user , whether it is y or n.
# accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
# if accept == "yes":
#     name = input("What is your name?\nName: ")
#     for emp_name in EMPLOYEES:
#         if name == emp_name:
#             print("Thank you " + emp_name + ", you are now checked in.")
#
#             # allows to the user to break out the loop
#             break
#     else:
#         print("You're not an employee")
#
# else:
#
#     print("This service is not for you. Exiting program...")
#     exit()






#option 2
# accept = input("Do you work for "+ COMPANY_NAME + "?\n (yes/no):")
# # using a boolean value to authenticate the employee within the Array.
# is_employee = False
#
# #empty string to store employee name
# employee_name = ""
#
# if accept =="yes":
#     name = input("What is your name?\n Name: ")
#     for emp_name in EMPLOYEES:
#         if name == emp_name:
#             is_employee = True
#             employee_name = emp_name
#
#     if is_employee:
#         print("Thank you " + employee_name +", You are checked in")
#     else:
#         print("Not an employee")
# else:
#     print("This service is not for you , Exiting Program...")
#     exit()


    #Option 3
    # accept = input(" DO you work for "+ COMPANY_NAME+" ?  \n (yes/no) ")
    # if accept == "yes":
    #     name = input("What is your name? \n Name: ")
    #     if name not in EMPLOYEES:
    #         print("You are not an employee")
    #     else:
    #         print("Thank you " + name +", you are now checked in,")
    #
    # else:
    #     print("This service is not for you, Exiting program...")
    #     exit()


#Bonuses

#Taking out trailing spaces//Ignoring captilization  bonuses 1 and 2.
accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
if accept == "yes":
    name = input("What is your name?\nName: ").strip().lower()
    for emp_name in EMPLOYEES:
        if name.casefold() == emp_name.casefold():
            print("Thank you " + emp_name + ", you are now checked in.")
            break
    else:
            print("You're not an employee")
else:
    print("This service is not for you. Exiting program...")
    exit()



#Allow all inputs that start with Y = yes  completed bonus 3/4

# accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ").lower()
# if accept.startswith("y"):
#     name = input("What is your name?\nName: ")
#     for emp_name in EMPLOYEES:
#         if name == emp_name:
#             print("Thank you " + emp_name + ", you are now checked in.")
#
#             break
#     else:
#             print("You're not an employee")
# else:
#     print("This service is not for you. Exiting program...")
#     exit()



# if user doesnt input yes or no  make them exit the program.

accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
if "y" != accept[0] and accept[0] != "n":
    name = input("What is your name?\nName: ")
    for emp_name in EMPLOYEES:
        if name == emp_name:
            print("Thank you " + emp_name + ", you are now checked in.")

            break
    else:
            print("You're not an employee")
else:
    print("This service is not for you. Exiting program...")
    exit()