from sys import argv

try:
    direction, output_hrs, rate_per_hrs, prize = argv
    output_hrs = int(output_hrs)
    rate_per_hrs = int(rate_per_hrs)
    prize = int(prize)
    if output_hrs >= 0 and rate_per_hrs > 0 and prize >= 0:
        salary = output_hrs * rate_per_hrs + prize
        print("Your salary is {}".format(salary))
    else:
        print("Number of worked hours, premium could not be less than 0. Rate per hours could not be less or equal than 0")
except ValueError:
    print("User, please enter the correct values or only 3 arguments")
