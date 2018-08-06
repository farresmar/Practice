import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv("Player-Data.txt")
fig, ax = plt.subplots()
groups = df.groupby("Pos")
for name, group in groups:
    ax.plot(group.PPG, group.FGPercentage, marker = "o", linestyle = " ", ms=10, label = name)
    ax.legend(numpoints=1)
    ax.set_ylim(-.2, 1.2)

ax.set_xlabel("Points per Game")
ax.set_ylabel("Field Goal Percentage")
ax.set_title("NBA Players PPG vs FG% for 2017-18 season")

plt.show()
