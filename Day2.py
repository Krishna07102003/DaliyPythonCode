percentage_marks=float(input("Enter your total percentage :"))
if percentage_marks>=90 and percentage_marks<=100:
    print("Grade A")
elif percentage_marks>=80 and percentage_marks<90:
    print("Grade B")
elif percentage_marks>=70 and percentage_marks<80:
    print("Grade C")
elif percentage_marks>=60 and percentage_marks<70:
    print("Grade D")
else:
    print("Fail")