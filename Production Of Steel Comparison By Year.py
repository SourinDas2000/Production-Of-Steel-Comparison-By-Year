
import matplotlib.pyplot as plt

import pandas as pd


plt.style.use("fivethirtyeight")


# Data :
    
data = pd.read_excel("Production Of Steel.xlsx")


# Plotting data :

plt.plot(data.Year, data.Production, marker = "o")

plt.fill_between(data.Year, data.Production, alpha = 0.25)

plt.title("Production Of Steel From Year 1990 To 1996")

plt.xlabel("Year >>>>")

plt.ylabel("Production >>>>")

plt.tight_layout()

plt.show()


''' Created By Sourin Das '''
