#if and else
#Date : 26/02/2024
#Name : Lawrence Mwariri

age = 17
if age > 18 :
    print("You are allowed to drive")

salary = 45000
if salary > 30000 and salary < 50000 :
    salary = salary * 0.1 + salary
    print(salary)

Home_county = "Nyeri"

if Home_county == "Nyeri" or Home_county == "Kisii" :
    print("You get a bursary")

grade = int(input("Enter the students grade : "))

if grade >=84 and grade<=90 :
    print("You win a calculator")
elif grade >=50 and grade <=83 :
    print("You win a mathematical set")
else :
    print("You get nothing ! ")