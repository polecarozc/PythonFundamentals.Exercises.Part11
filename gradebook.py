
class AliveStatus:
    #0 DEAD 1 ALIVE
    alive_status = None

class person:
    def __init__(self, first_name, last_name, dob, alive_status):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive_status = alive_status

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_status):
        self.alive_status = new_status

class instructor(person):
    def __init__(self, instructor_id):
        self.instructor_id = instructor_id

class student(person):
    def __init__(self, student_id):
        self.student_id = student_id

class zipcode_student(student):
    pass

class college_student(student):
    pass

class classroom:
    def __init__(self):
        self.students = []
        self.instructors = []
    def add_instructor(self, instructor_name):
        self.instructor_name = instructor_name
        self.instructors.append(instructor_name)
    def remove_instructor(self, instructor_name_to_remove):
        self.instructor_name_to_remove = instructor_name_to_remove
        self.instructors.remove(instructor_name_to_remove)

    def add_student(self, name):
        self.name = name
        self.students.append(name)

    def remove_student(self, name_to_remove):
        self.name_to_remove = name_to_remove
        self.students.remove(name_to_remove)

    def print_instructors(self):
        print(self.instructors)

    def print_students(self):
        print(self.students)


