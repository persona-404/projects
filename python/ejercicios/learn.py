#### strs
#ask users name
"""
name = input("What's your name?").strip() # removes spaces

# remove spaces
print(f"hello, {name}")

# split users name into parts
first, last = name.split(" ")
print(first, last)
"""

"""
def hello(to = "world", times = 3):
    print(f"hello {to}\n" * times, end="") # so the last one doesnt print \n

hello("alylu", 5)
"""

students = ["s1", "s2", "s3"]

for student in students:
    print(student)

for i in range(len(students)):
    print(f"{i}:", students[i])

students = {
    "s1": "x1",
    "s2": "x2"
}

for student in students:
    print(student, students[student], sep=": ") # char to add between values
