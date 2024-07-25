grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
student0 = sum(grades[0])/len(grades[0])
student1 = sum(grades[1])/len(grades[1])
student2 = sum(grades[2])/len(grades[2])
student3 = sum(grades[3])/len(grades[3])
student4 = sum(grades[4])/len(grades[4])
ave_grades = [student0, student1, student2, student3, student4]
students = {'Johnny', 'Bilbo', 'Stive', 'Khendrik', 'Aaron'}
list_stud = list(students)
list_stud.sort()
class_reg = {list_stud[0] : ave_grades[0], list_stud[1] : ave_grades[1], list_stud[2] : ave_grades[2], list_stud[3] : ave_grades[3], list_stud[4] : ave_grades[4]}
print(class_reg)