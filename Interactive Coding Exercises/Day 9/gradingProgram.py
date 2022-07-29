student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇\
# For each name(key) in student_scores
for sName in student_scores:   # s_Name is the key in student_scores. "Harry"
  score = student_scores[sName]  # Get the value of the name and put it in score.

  if score > 90:  # If score > 90.
    student_grades[sName] = "Outstanding" # Add the name(key) in student_scores to student_grades with the value of "Outstanding"
  elif score > 80:
    student_grades[sName] = "Exceeds Expectations" # {"Harry": "Exceeds Expectations"}
  elif score > 70:
    student_grades[sName] = "Acceptable"  # {"Ron": "Acceptable"}
  else:
    student_grades[sName] = "Fail" # {"Neville": "Fail"}


# 🚨 Don't change the code below 👇
print(student_grades)
