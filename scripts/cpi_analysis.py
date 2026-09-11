import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data/raw/vietnam_cpi.xlsx")

# Filter analysis period
df = df[(df["Year"] >= 2019) & (df["Year"] <= 2025)]

# Display data
print(df)

# Create line chart
plt.figure(figsize=(9, 5))

plt.plot(
    df["Year"],
    df["CPI (2010 = 100)"],
    marker="o"
)

plt.title("Vietnam Consumer Price Index (2019–2025)")
plt.xlabel("Year")
plt.ylabel("CPI (2010 = 100)")

plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig("figures/cpi_trend.png", dpi=300)

plt.show()