# project: student marks CSV

'''Create `students.csv` with at least 10 rows and columns `name,subject,marks,city`. Load it with `pd.read_csv`. Find total rows,
average marks, highest scorer, marks below 40, average marks by city and subject-wise count. Save cleaned data with
`df.to_csv('clean_students.csv', index=False)`.'''

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "student.csv")

print(df.head())

df["marks"] = df["marks"].fillna(df["marks"].median())
print("Total Students : " ,len(df))
print("Average Marks : ", df["marks"].mean())
print("\n Highest Scorer")
print(df.loc[df["marks"].idxmax()])
print("\n Student below 40 marks ")
print([df["marks"]<40])
print("\n Average marks by city")
print(df.groupby("city")["marks"].mean())
print("\n Student per Subject")
print(df["subject"].value_counts())
df.to_csv( BASE_DIR / "clean student.csv",index=False)
print(df)
print("\n cleaned csv saved successfully!")


#Matplotlib
#charts
import matplotlib.pyplot as plt
days = ["mon","tue","wed","thu","fri"]
steps = [3000,2000,6000,4000,5000,]
plt.plot(days,steps,marker="o")
plt.title("steps during a week")
plt.xlabel("days")
plt.ylabel("steps")
plt.grid(True)
plt.show()
plt.bar(days,steps)
plt.show()
plt.scatter(range(5),steps)
plt.show()
plt.hist(steps,bins=5)
plt.show()

#Seaborn
#statistical chart
