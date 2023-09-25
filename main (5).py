#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. 
class Student:
  def __init__(self, name,roll_number, cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  Sorted_Students=sorted(student_list,
                      key=lambda student: student.cgpa,
                      reverse=True)
  return Sorted_Students
students=[Student("Hari", "A123", 9.7),
         Student("Gokul", "A126", 8.5),
         Student("Deva", "A125", 9.5),
         Student("Aravind", "A126", 8.7)]
Sorted_Students=sort_students(students)

#print the sorted llist of students:
for student in Sorted_Students:
  print("Name: {}, Roll Number: {}, CGPA:{}".format(student.name, student.roll_number, student.cgpa))