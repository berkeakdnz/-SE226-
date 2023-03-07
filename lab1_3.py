name = input('What is your name ?')
lab_grade = int(input("Enter lab grade (out of 100): "))
midterm_grade = int(input("Enter midterm grade (out of 100): "))
final_grade = int(input("Enter final grade (out of 100): "))

last_score = lab_grade*0.25 + midterm_grade*0.35 + final_grade*0.4

print("Name:", name)
print("Lab:", lab_grade)
print("Midterm:", midterm_grade)
print("Final:", final_grade)
print("Last Score:", last_score)
