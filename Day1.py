# Student Performance Analyzer

StudentName = input("Enter the student's name: ")
RollNumber = input("Enter the student's roll number: ")
Branch = input("Enter the student's branch: ")
NumberOfSubjects = int(input("Enter the number of subjects: "))

marksList = []
weakSubjects = []

for i in range(NumberOfSubjects):
    mark = int(input(f"Enter marks for Subject {i+1}: "))
    marksList.append(mark)

    if mark < 50:
        weakSubjects.append(f"Subject {i+1}")

# Calculations
Totalmarks = sum(marksList)
AverageMarks = Totalmarks / NumberOfSubjects
HighestMark = max(marksList)
LowestMark = min(marksList)
Percentage = AverageMarks

# Grade Calculation
if Percentage >= 90:
    Grade = "A+"
elif Percentage >= 80:
    Grade = "A"
elif Percentage >= 70:
    Grade = "B"
elif Percentage >= 60:
    Grade = "C"
elif Percentage >= 50:
    Grade = "D"
else:
    Grade = "Fail"

# Result
if Percentage >= 50:
    Result = "PASS"
else:
    Result = "FAIL"

# Feedback
if Grade == "A+":
    Feedback = "Outstanding performance."
elif Grade == "A":
    Feedback = "Excellent performance. Keep it up!"
elif Grade == "B":
    Feedback = "Good performance. Improve consistency."
elif Grade == "C":
    Feedback = "Average performance. More practice needed."
elif Grade == "D":
    Feedback = "Needs improvement. Work harder."
else:
    Feedback = "Poor performance. Focus on studies."

# Report
print("\n----- Student Performance Report -----")

print("Name:", StudentName)
print("Roll No:", RollNumber)
print("Branch:", Branch)

print("\nMarks:", marksList)

print("Total Marks:", Totalmarks)
print("Average Marks:", round(AverageMarks, 2))
print("Highest Mark:", HighestMark)
print("Lowest Mark:", LowestMark)
print("Percentage:", round(Percentage, 2), "%")

print("\nGrade:", Grade)
print("Result:", Result)

if len(weakSubjects) > 0:
    print("Subjects Needing Improvement:", ", ".join(weakSubjects))
else:
    print("Subjects Needing Improvement: None")

print("\nFeedback:", Feedback)

# Slicing Examples
print("\n----- Marks Analysis -----")

print("First 3 Subject Marks:", marksList[:3])
print("Last 2 Subject Marks:", marksList[-2:])