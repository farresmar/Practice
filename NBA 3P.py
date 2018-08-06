import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv("Player-Data.txt")
fig, ax = plt.subplots()
my_scatter_plot = ax.scatter(
    df["PPG"],
    df["FGPercentage"],
    c=df["3P"],
    cmap=plt.cm.Reds,
    vmin=0,
    vmax=df["3P"].max(),
    edgecolor="#6b0c08",
    linewidth=.75
    )

cbar = fig.colorbar(my_scatter_plot)
cbar.set_label("Number of 3-pointers made per game")

ax.set_xlabel("Points per Game")
ax.set_ylabel("Field Goal Percentage")
ax.set_title("NBA Players PPG vs FG% for 2017-18 season")

plt.show()
