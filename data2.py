import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = px.bar(x=df["height"].tolist(), y=df["index"].tolist())
fig.show()