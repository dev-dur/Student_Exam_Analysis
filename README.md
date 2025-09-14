# 📊 Student Exam Analysis

This is a beginner-friendly **data analysis mini-project** using **NumPy, Pandas, and Matplotlib**.
The project generates random student exam scores, analyzes them, and visualizes the results.

## 🚀 Features

* Generate random student scores with **NumPy**
* Store and analyze data using **Pandas DataFrame**
* Calculate statistics (average, max, min)
* Visualize exam results with **Matplotlib bar charts**
* Save figures as `.png` files in the same folder

## 🛠 Tech Stack

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)

## 📂 Project Structure

```
student-exam-analysis/
│
├── student_analysis.py    # Main project script
├── student_scores.png     # Saved figure (auto-generated)
└── requirements.txt       # Dependencies
 
```

## ⚡ How to Run

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/student-exam-analysis.git
   cd student-exam-analysis
   ```
2. Install requirements:

   ```bash
   pip install numpy pandas matplotlib
   ```
3. Run the script:

   ```bash
   python student_analysis.py
   ```
4. Check the saved figure:

   * `student_scores.png` will be created in the same folder.


## 📊 Example Output

**Console Output**

```
Student Data:
     Name  Math  Science
0    Ali    88       92
1   Sara    70       53
...
```

**Figure Output**
A bar chart comparing Math and Science scores for each student.

---

## 🎯 Future Improvements

* Load student data from a CSV file
* Add more subjects (English, History, etc.)
* Generate summary reports
* Export results to Excel
