#EX1: program asking input for customer for number of videos purchased
# output being points earned

# input:
points = int(input("Enter the no of video purchased"))

#conditions with its output
if points == 0:
    print("The earning is 0 points")
elif points == 1:
    print("The earning is 5 points")
elif points == 2:
    print("The earning is 15 points")
elif points == 3:
    print("The earning is 30 points")
elif points >= 4:
    print("The earning is 60 points")
    
    
#EX 2: Calculate BMI using height and weight of user

#input user's height and weight
user_height = float(input("Enter your height in meter's"))
user_weight = float(input("Enter your weight in kgs"))

# Creating a function for BMI
def bmi(x = float, y = float) ->float:
    result = round((x/y**y), 2)
    return(result)

my_bmi = bmi(x = user_weight, y = user_height)

if my_bmi < 18.5:
    print("Your BMI is: ", my_bmi)
    print("You are underweight") 
elif  my_bmi>=18.5 and my_bmi <= 24.99:
    print("Your BMI is: ", my_bmi)
    print("You have normal weight")
elif  my_bmi>=25.00 and my_bmi <= 29.99:
    print("Your BMI is: ", my_bmi)
    print("You are overweight")    
elif my_bmi > 30:
    print("Your BMI is: ", my_bmi)
    print("You are obese")

#EX 3: Calculating Property tax from actual value of property

#Asking for Actual value of propert as input
actual_value = int(input("Enter the actual value of your property"))

# calculating assesment value
assesment_value = 0.6 * actual_value

# propert tax function
def property_tax(b = int) ->float:
    result = (72*(b / 100))/100
    print(f"The assesment vlue of the property is: ${b}")
    print(f"The property tax of the property is: ${result}")

property_tax(b = assesment_value)

# EX4: SUM of numbers:

#initialize a variable
total_sum = 0

number = float(input("Enter a positive number (enter a negative number to end): "))
while number >= 0:
    total_sum += number
    number = float(input("Enter a positive number (enter a negative number to end): "))

print("Total sum is: ", total_sum )


# EX 5: Maximum of two values

# asking for input of two integer values
a = int(input("Enter a number"))
b = int(input("Enter another number"))

c = [a, b]

# function
def my_max(c = int) -> int:
    d = max(c)
    print("The greatest of the two numbers is: ", d)

# to find the greatest between the two numbers
my_max(c)

# EX: 6 Calculating average from 5test score and grading them respectively

# Inputting scores
scores = []

for x in range(5):
    ts = int(input("Enter your test score from 0 to 100"))
    scores.append(ts)
print("Scores entered: ", scores)

# function for average from the test scores
def calc_average(scores = list) -> float:
    average=sum(scores)/len(scores)
    return(average)

#assigning a variable for the average calculated
my_avg = calc_average(scores)
scores.append(my_avg)

# function for assigning grade to test scores
def determine_grade(scores = list) -> list:
    grade=[]
    for x in range(6):
        if scores[x] >= 90 and scores[x] <= 100:
            grade.append("A")
        elif scores[x]>= 80 and scores[x] <= 89:
            grade.append("B")
        elif scores[x] >= 70 and scores[x] <= 79:
            grade.append("C")
        elif scores[x] >= 60 and scores[x] <= 69:
            grade.append("D")
        else:
            grade.append("F")
    return(grade)

grade_list = determine_grade(scores)

for x in range(6):
    if x<5:
        print(f"The test score {scores[x]} is graded {grade_list[x]}")
    else:
        print(f"The average score {scores[x]} is graded {grade_list[x]}")
