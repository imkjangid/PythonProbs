# Real-World Example: Classroom vs. School Bag

school_name = "Greenwood High" # GLOBAL: Everyone in the school knows it.

def classroom_one():
    student_bag = "Geometry Box" # LOCAL: Only visible inside this classroom.
    
    print("School Name (Global):", school_name)
    print("Inside Classroom (Local):", student_bag)

print("School Name (Global):", school_name) # Output: Greenwood High
classroom_one()
print("student bag (Local):", student_bag) # Output: NameError: name 'student_bag' is not defined