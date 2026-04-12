import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [2, 3, 1.5, 4, 2.5, 3.5, 2]

plt.figure(figsize=(8,5))

plt.plot(days, hours, marker='o')

plt.title("My Study Hours This Week")
plt.xlabel("Days")
plt.ylabel("Hours")

plt.grid()

plt.savefig("study_chart.png")
plt.show()