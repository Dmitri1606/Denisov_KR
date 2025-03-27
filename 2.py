import pandas as pd
import matplotlib.pyplot as plt

df_excel = pd.read_excel("Книга111.xlsx")
df = pd.read_excel("Книга11.xlsx")

x = df_excel["X"]
y = df_excel["Y"]
X = 30
Y = 20

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))

#1
ax1.hist([x, y], color=['red','green'], edgecolor='black', bins=10, label=['X', 'Y'])
ax1.set_title('Гистограмма X и Y')
ax1.set_xlabel('Значения')
ax1.set_ylabel('Частота')
ax1.legend()
ax1.grid(True)
#2
ax2.pie([X, Y])
ax2.set_title('Сравнение средних значений')
ax2.legend("XY")
#3
ax3.boxplot([x], vert=True, patch_artist=True)
plt.title('Ящик с усами для столбца X')
plt.ylabel('Значения')
plt.grid(True)
plt.tight_layout()
plt.show()
