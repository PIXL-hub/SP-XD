                     #برنامج يقوم بحساب عدد الطلاب الناجحين و الراسبين و يضيف 5 درجات لكل طالب قبل استخراج النتائج

Grades = [21,64,82,34,34,86,31,48,62,58,94,71,29,13,44,17,20]
Passed_Student = 0
Failed_Student = 0
New_Grades = []
for mark in Grades:
    if mark >= 50:
        Passed_Student += 1
    elif mark <= 50:
        Failed_Student += 1
    else:
        print("Student don't found")

print("The passed student are: ",Passed_Student)        
print("The failed student are: ",Failed_Student)


for mark in Grades:
    Bouns = mark+5
    New_Grades.append(Bouns)

print("Original Grades: ",Grades)
print("Grades After the bouns: ",New_Grades)