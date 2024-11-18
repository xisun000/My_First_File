StudentId = {
    "101" :"Xisun Akon",
    "102" :"Radoan Akon",
    "103" :"Rezual Akon",
    "104" :"Ruma Akter",
}
print(StudentId.get("104","not a valid key"))


stu = []

for student in enumerate(StudentId):
    if student[1] == '101':
        stu.append(student[1])
        print(stu)

for student in range(len(StudentId)):
    stu.append(student)
    print(stu)

list = [2, 4, 6, 9, 11, 12, 10]

for i in range(len(list)):
    for j in range(len(list)+1):
        print("Original String: ", str(i))

sorted = sorted([x for x in list])
print(sorted)


