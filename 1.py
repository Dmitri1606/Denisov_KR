import pandas as pd
df_excel = pd.read_excel('Книга 3 (1) (5).xlsx')
print(df_excel)

vertical=int(input("ведите значение координат по вертикали начиная с 0:"))
horizontal=int(input("ведите значение координат по горизонтали начиная с 0:"))
word=str(input("Ведите на что хотите заменить значение:"))

change=df_excel.iat[vertical, horizontal] = word

print(df_excel)