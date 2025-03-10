# Plotting a linegraph on python
#By Hlanhla Hlungwane
#10 March 2024

#import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import lineStyles

plt.style.use('default')

#import excel file
beverages = pd.read_excel("Hot_Beverages.xlsx")
print(beverages.head(5))

#plotting a line graph

plt.plot(beverages["Year"], beverages["Coffee"], linestyle ='solid', linewidth = 3,
         marker='>', markersize = 7, label ='coffee')
plt.plot(beverages["Year"], beverages["Tea"], linestyle ='dotted', linewidth =3,
         marker='D', markersize = 7, label = 'Tea')
plt.title("The amount of Coffee or Tea per Year")
plt.xlabel("Year")
plt.ylabel("Number of times Drank")
plt.legend(loc = 'lower right')
plt.grid()
plt.show()

