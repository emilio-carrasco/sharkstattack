import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.gridspec as gridspec
import numpy as np

df = pd.read_csv("./outputs/anyos_out.csv",encoding = "ISO-8859-1")


fig3 = plt.figure(constrained_layout=True)
fig3.set_size_inches(7, 7)

gs = fig3.add_gridspec(3,3)

f3_ax1 = fig3.add_subplot(gs[0,:])
f3_ax1.set_title('#Ataques')

f3_ax2 = fig3.add_subplot(gs[1,:])
f3_ax2.set_title('Δ Temperatura')

f3_ax3 = fig3.add_subplot(gs[-2:-1])
f3_ax3.set_title('Diagrama de dispersíon')




f3_ax1.plot(df.Years, df.Attacks, 'tab:red')
f3_ax2.plot(df.Years, df['10yvariation'])
f3_ax3.scatter( df.Attacks, df['10yvariation'], c="green")

correlacion=df[['10yvariation','Attacks']].corr()
corre=correlacion.Attacks['10yvariation']
print(round(corre,2))
f3_ax3.annotate(f"Correlación = {corre}", xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

z = np.polyfit(df.Attacks, df['10yvariation'], 1)
p = np.poly1d(z)
plt.plot(df.Attacks,p(df.Attacks),"r. ", alpha=0.5)

plt.show()


fig3.savefig('./fig/attacks-temp.png')

