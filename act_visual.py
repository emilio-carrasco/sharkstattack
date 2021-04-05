import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("./outputs/act_out.csv",encoding = "ISO-8859-1")

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(y = 'Activity', data = df, order = df['Activity'].value_counts(ascending=True).index, hue=df.Sex, palette="Blues")
plt.savefig('./fig/act.png')