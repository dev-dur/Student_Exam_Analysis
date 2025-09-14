import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generate random scores for 10 students
np.random.seed(42)
names = ["ali", "saad", "fahad", "zainab", "noor", "sara", "Hassan", "Maya", "Bilal", "Zara"]

# 2. Generate 10 random integers between 50 and 99.
math_scores = np.random.randint(50, 100, size=10)
science_scores = np.random.randint(50, 100, size=10)

# 3. Put into Pandas DataFrame
df = pd.DataFrame({
    "Name": names,
    "Math": math_scores,
    "Science": science_scores})
print("Student Data:\n", df)

# 3. Analysis
print("\nAverage Math Score:", df["Math"].mean())
print("Highest Science Score:", df["Science"].max())

# 4. Visualization figure (chart canvas) with width=8, height=5
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Math"], label="Math")
# alpha=0.7 (slightly transparent so both sets of bars can be seen)
plt.bar(df["Name"], df["Science"], alpha=0.7, label="Science")

plt.title("Student Exam Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.legend() # shows labels ("Math" and "Science") at the side.

# Save figure
plt.savefig("student_scores.png", dpi=300, bbox_inches="tight")  
plt.show()