import matplotlib.pyplot as plt
import pandas as pd

subject = input("MATHEMATICS, PHYSICS, CHEMISTRY")
roll_number = int(input("Roll No: "))
data_processed_path = f"Data/Processed/{subject}/{roll_number}.csv"

student_data = pd.read_csv(data_processed_path)

names = ["Student", "Class"]
values = [student_data["Avg_of_test"][0], student_data["Avg_class"][0]]
plt.grid(visible=True)
plt.bar(names, values)
# plt.subplot(131)
plt.suptitle("Student v/s Class")
plt.show()
