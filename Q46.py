marks = []
for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i + 1}: ")))
print("Total:", sum(marks))
