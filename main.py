import pandas as pd
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# pull out columns
subset = df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

# plot
plt.plot(
    subset["Mortality rate, infant (per 1,000 live births)"],
    subset["GDP per capita (constant 2010 US$)"],
    "ro",
)
plt.show()
