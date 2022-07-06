# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Do not use these:
# Max () - returns the highest number.
# Min() - returns the lowest number.

max_score = 0  # Store the highest_score in the list.

for score in student_scores:  # For each score in the list:
    if score > max_score:  # If the score is greater than the max_score,
        max_score = score  # Save the score in the max_score.

print(f"The highest score in the class is: {max_score}")
