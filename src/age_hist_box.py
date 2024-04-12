import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

age_df = pd.read_csv("age.csv")

mean = age_df['age'].mean()
median = age_df['age'].median()
mode = age_df['age'].mode()
 
fig, (ax_box, ax_hist) = plt.subplots(2, gridspec_kw={"height_ratios": (.15, .85)}, figsize = (16,8))
 
sns.histplot(age_df['age'],
             binwidth = 1,
             ax = ax_hist, 
             color= '#ff774a', 
             kde=False)

sns.boxplot(age_df['age'], 
            ax = ax_box,
            color = '#ff774a',
            orient ='h')

ax_hist.axvline(mean, color = 'r', linewidth = 4)

ax_hist.axvline(median, color = 'black', linestyle = 'dashed', linewidth = 3)

for m in mode:
    ax_hist.axvline(m, color = "#20a483", linestyle = 'dashed', linewidth = 3)


for ax in (ax_hist, ax_box):
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

ax_box.set(xlabel=None)

# Hide Y axes tick marks
ax_box.set_yticks([])

# Use plt.sca to set the current axes for the pyplot state machine (i.e. the plt interface).

plt.yticks(fontsize = 14, family = 'monospace')

plt.xticks(fontsize = 14, family = 'monospace')

plt.xlabel("age", fontsize = 14)

plt.suptitle("Age distribution (in years)", fontsize = 18, family = 'monospace')

plt.legend({'Mean':mean,
            'Median':median,
            'Mode':mode}, 
            ncol=3, 
            bbox_to_anchor=(0.7,-0.15),
            fontsize=15)

plt.savefig("age.png", bbox_inches = "tight")
