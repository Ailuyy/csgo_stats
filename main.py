import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

main = open("main.json", "r").read()
dcm = json.loads(main)
tmp = dcm.get("playerstats").get("stats")

main_A = []
main_B = []
main_C = []

for dic in tmp:
    name = dic["name"]
    value = dic["value"]

    if name in ["total_kills", "total_deaths"]:
        main_A.append(value)
    elif name in ["total_planted_bombs", "total_defused_bombs"]:
        main_B.append(value)
    elif name in ["total_time_played", "total_wins"]:
        if name == "total_time_played":
            value /= 60 # sec to min
        main_C.append(value)

graph_data_labels = ["total_kills", "total_deaths", "total_planted_bombs", "total_defused_bombs", "total_time_played", "total_wins"]
all_main = main_A + main_B + main_C
#graphs
barWidth = 0.3

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

bar_m_A = np.arange(len(main_A))
axs[0].bar(bar_m_A, main_A, color="g", width=0.4, edgecolor="black", label="main")
axs[0].set_xticks(bar_m_A)
axs[0].set_xticklabels(graph_data_labels[0:2])
axs[0].legend()
axs[0].set_title("Total kills and deaths")

bar_m_B = np.arange(len(main_B))
axs[1].bar(bar_m_B, main_B, color="g", width=0.4, edgecolor="black", label="main")
axs[1].set_xticks(bar_m_B)
axs[1].set_xticklabels(graph_data_labels[2:4])
axs[1].legend()
axs[1].set_title("Total planted and defused bombs")

bar_m_C = np.arange(len(main_C))
axs[2].bar(bar_m_C, main_C, color="g", width=0.4, edgecolor="black", label="main")
axs[2].set_xticks(bar_m_C)
axs[2].set_xticklabels(graph_data_labels[4:6])
axs[2].legend()
axs[2].set_title("Total time played (min) and total won rounds")

#stats.to_csv
merged_dict = {}
for i, x in enumerate(graph_data_labels):
    merged_dict[x] = [all_main[i]]

df = pd.DataFrame.from_dict(merged_dict, orient="index", columns=["main_acc"]).astype(int)
df.to_csv("stats_python.csv", sep=";")

plt.savefig("charts.png")
plt.show()
