student_marks.py

import matplotlib.pyplot as plt

# Student marks data
students = ["Aman", "Divya", "Rohit", "Sneha", "Kiran"]
marks = [85, 92, 76, 88, 95]

# Create bar chart
plt.bar(students, marks)
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)

# Show graph
plt.show()
