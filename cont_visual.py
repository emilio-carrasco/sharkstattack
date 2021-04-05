import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("./outputs/cont_out.csv",encoding = "ISO-8859-1")
# set the figure size
plt.figure(figsize=(10,5))
# draw the chart
g = sns.countplot(
    data=df,
    x='Continent',
    hue='Gender',
    palette='Set2',
    )
g.set_xticklabels(g.get_xticklabels(),
                  rotation=10,
                 fontweight='light',
                fontsize='large')
plt.savefig('./fig/cont.png')