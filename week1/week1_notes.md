# Week 1 - Vietnam CPI and Inflation

## A. CPI Fundamentals

### 1. What is CPI?

CPI (Consumer Price Index) is an index that measures how the prices of a basket of goods and services purchased by consumers change over time.

### 2. What does CPI measure?

CPI measures the change in consumer prices over time. It helps us understand whether the general price level is increasing or decreasing.

### 3. What goods and services are included in CPI?

- Food and beverages
- Housing
- Transportation
- Healthcare
- Education
- Clothing
- Other consumer goods and services

### 4. How is CPI calculated?

CPI compares the cost of a basket of goods and services in the current period with the cost of the same basket in a base period.

### 5. What is a base year?

A base year is the reference year used to compare price changes.

In my dataset:

**Base year = 2010, where CPI = 100.**

e.g: if CPI = 150, the general price level is about 50% higher than in the base year.
## B. Inflation

### 6. What is inflation?

Inflation is the rate at which the general level of prices of goods and services increases over time.

When inflation is positive, consumers generally need more money to buy the same basket of goods and services than before.

### 7. Are CPI and inflation the same?

No.

CPI is an index that represents the general price level relative to a base year.

Inflation is the percentage change in CPI between two periods.

For example:

- CPI in 2024 = 189.70
- CPI in 2025 = 195.98

CPI increased, while the inflation rate describes how fast CPI increased from 2024 to 2025.

### 8. How is inflation calculated?

The inflation rate can be calculated using:

Inflation Rate = ((CPI current - CPI previous) / CPI previous) × 100

For example, if:

- Previous CPI = 110
- Current CPI = 114

Then:

Inflation = ((114 - 110) / 110) × 100

Inflation ≈ 3.64%

### 9. Can CPI increase while inflation decreases?

Yes.

CPI can continue increasing while inflation decreases.

This means prices are still increasing, but they are increasing at a slower rate than before.

For example:

- Year 1 inflation = 6%
- Year 2 inflation = 3%

Prices still increased in Year 2, but the speed of price growth became slower.

### 10. If inflation falls from 6% to 3%, are prices falling?

No.

A fall in inflation from 6% to 3% means prices are still increasing, but at a slower rate.

Prices would generally be falling if the inflation rate became negative, which is called deflation.
## C. Data Understanding

### 11. Where does the dataset come from?

The dataset contains Consumer Price Index (CPI) & Inflation rate data for Vietnam.

Source: World Bank 

### 12. What is the frequency of the dataset?

The dataset has annual frequency.

Each observation represents one year.

Because the data is annual, it is useful for observing long-term CPI and inflation trends. However, it cannot show short-term monthly price movements.

### 13. What does one row represent?

Each row represents one year of CPI and inflation data for Vietnam.

### 14. What are the main variables?

The main variables are:

| Variable | Type | Description |
|---|---|---|
| Year | Numerical / Time | The year of observation |
| CPI (2010 = 100) | Numerical | Consumer Price Index, using 2010 as the base year |
| Inflation | Numerical | Annual percentage change in the CPI |

### 15. Are there missing or unusual values?

The dataset does not contain missing values in the main variables.

The CPI values generally increase over time.

Inflation changes from year to year, which is expected because the rate of price growth is not constant.