Marks=60
if 80<=Marks<=100:
    print("Outstanding")
    print("Gradepoint 10")
    print("GPA 10")
elif 70<=Marks<=79.99:
    print("Excellent")
    print("Gradepoint 9")
    print("GPA 9")
elif 60<=Marks<=69.99:
    print("VeryGood")
    print("Gradepoint 8")
    print("GPA 8")
elif 55<=Marks<=59.99:
    print("Good") 
    print("GradePoint 7") 
    print("GPA 7")
elif 50<=Marks<=54.99:
    print("Average")
    print("GradePoint 6")
    print("GPA 6.0 to 6.99")
elif 45<=Marks<=49.99:
    print("Below Average")
    print("GradePoint 5 ")
    print("GPA 5.0 to 5.99 ")
elif 40<=Marks<=44.99:
    print("GradePoint 4 ") 
    print("GPA 4.0 to 4.99 ")
    print("PASS")
elif 39.99<=Marks<=35:
    print("GradePoint 0 ")
    print("FAIL")
else:
    print("Invalid Message")      