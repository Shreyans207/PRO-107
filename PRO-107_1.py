import pandas as pd
import plotly.express as px
import statistics

read = pd.read_csv('PRO-107_2.csv')

Roll_No = read['Roll No'].to_list()
Marks_In_Percentage = read['Marks In Percentage'].to_list()
Days_Present = read['Days Present'].to_list()

mean1 = statistics.mean(Marks_In_Percentage)
mean2 = statistics.mean(Days_Present)

scatter = px.scatter(read , x = Roll_No , y = Marks_In_Percentage , color = Days_Present)
scatter.show()

print(mean1)
print(mean2)
