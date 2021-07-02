import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
#fig = px.bar(x=df["height"].tolist(), y=df["index"].tolist())
#fig.show()

height_list = df["height"].tolist()
mean = statistics.mean(height_list)
mode = statistics.mode(height_list)
median = statistics.median(height_list)
standard_deviation = statistics.stdev(height_list)

print(f"mean: {mean}")
print(f"mode: {mode}")
print(f"median: {median}")
print(f"standard_deviation: {standard_deviation}")

first_standard_deviation_left, first_standard_deviation_right = mean - standard_deviation, mean + standard_deviation
second_standard_deviation_left, second_standard_deviation_right = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_standard_deviation_left, third_standard_deviation_right = mean - (3*standard_deviation), mean + (3*standard_deviation)

fig = ff.create_distplot([df["height"].tolist()], ["Height"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.3], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_left, first_standard_deviation_left], y = [0, 0.3], mode = "lines", name = "first_standard_deviation_left"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_right, first_standard_deviation_right], y = [0, 0.3], mode = "lines", name = "first_standard_deviation_right"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_left, second_standard_deviation_left], y = [0, 0.3], mode = "lines", name = "second_standard_deviation_left"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_right, second_standard_deviation_right], y = [0, 0.3], mode = "lines", name = "second_standard_deviation_right"))
fig.add_trace(go.Scatter(x = [third_standard_deviation_left, third_standard_deviation_left], y = [0, 0.3], mode = "lines", name = "third_standard_deviation_left"))
fig.add_trace(go.Scatter(x = [third_standard_deviation_right, third_standard_deviation_right], y = [0, 0.3], mode = "lines", name = "third_standard_deviation_right"))
fig.show()

data_within_first_standard_deviation = [result for result in height_list if result>first_standard_deviation_left and result<first_standard_deviation_right]
percentage_of_data_inFirst = len(data_within_first_standard_deviation)*100/len(height_list)
print(f"{percentage_of_data_inFirst}% lie_within_first_standard_deviation")

data_within_second_standard_deviation = [result for result in height_list if result>second_standard_deviation_left and result<second_standard_deviation_right]
percentage_of_data_inSecond = len(data_within_second_standard_deviation)*100/len(height_list)
print(f"{percentage_of_data_inSecond}% lie_within_second_standard_deviation")

data_within_third_standard_deviation = [result for result in height_list if result>third_standard_deviation_left and result<third_standard_deviation_right]
percentage_of_data_inThird = len(data_within_third_standard_deviation)*100/len(height_list)
print(f"{percentage_of_data_inThird}% lie_within_Third_standard_deviation")

