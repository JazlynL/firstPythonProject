import array

print("My First CLI in python")

#name = input("What is your name ? \n Your Name:")
#print("Hello" + name)



careerdevs = ["Gabriel", "cliff", "Jessie"]

accept = input("Do you Work for CareerDevs \n (yes/no) ")
if accept =="yes":
    name = input("What Is you Name?: ")
    for emp_name in careerdevs:
        if name == emp_name:
            print("Okay you got a job")
        else:
            print("you're not an employee")



else:

  print("Okay, you can leave")