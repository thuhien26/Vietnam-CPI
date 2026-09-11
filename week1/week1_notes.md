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


## D. Dataset Exploration

### Dataset Overview

The dataset contains annual CPI and inflation data for Vietnam.

- Number of observations: 30
- Number of variables: 3
- Time period: 1996-2025
- Frequency: Annual
- CPI base year: 2010 = 100

### Variables

| Variable | Type | Meaning |
|---|---|---|
| Year | Time / Numerical | Year of the observation |
| CPI (2010 = 100) | Numerical | Consumer Price Index relative to the 2010 base year |
| Inflation | Numerical | Annual percentage change in consumer prices |


### Analysis Period

For Week 1, the main analysis focuses on the period from 2019 to 2025.

| Year | CPI | Inflation |
|---|---:|---:|
| 2019 | 163.52 | 2.80% |
| 2020 | 168.78 | 3.22% |
| 2021 | 171.88 | 1.83% |
| 2022 | 177.31 | 3.16% |
| 2023 | 183.07 | 3.25% |
| 2024 | 189.70 | 3.62% |
| 2025 | 195.98 | 3.31% |

### Initial Observations

CPI increased every year between 2019 and 2025.

However, the inflation rate did not increase continuously. It decreased significantly in 2021, increased again between 2022 and 2024, and then decreased slightly in 2025.

This shows that CPI and inflation describe related but different aspects of price changes.
## Preliminary Findings

1. Vietnam's CPI increased continuously from 2019 to 2025.

2. CPI rose from approximately 163.5 in 2019 to about 196.0 in 2025.

3. The increase was relatively slower between 2020 and 2021 compared with later years.

4. CPI increased more strongly from 2022 onward.

5. Although CPI increased every year, the inflation rate did not follow the same pattern, showing that the price level and the rate of price growth are different concepts.
## D. Data Analysis Thinking

### 16. Which period from 2019 to the present is most noticeable?

The period from 2022 to 2024 is particularly noticeable because CPI increased more rapidly compared with the earlier period.

### 17. Does CPI increase evenly over time?

No. CPI generally increases over time, but the rate of increase is not constant. Some years show slower increases while others show faster increases.

### 18. Is CPI alone enough to conclude that people are living worse?

No. CPI only measures changes in consumer prices. To assess whether people are living worse, other indicators such as income, wages, employment, and purchasing power should also be considered.

### 19. What other variables would be useful?

- Income
- Wages
- GDP
- Unemployment
- Food prices
- Housing costs
## E. Critical Thinking

### 20. "CPI increased, therefore Vietnamese people are becoming poorer." Do you agree?

Not necessarily.

A higher CPI means prices have increased, but it does not directly mean people are poorer. We also need to consider income, wages, employment, and purchasing power.

### 21. What is more dangerous for a Data Analyst: not knowing a tool or misunderstanding the data?

Misunderstanding the data is more dangerous.

Tools can be learned, but misunderstanding variables, units, or concepts can lead to incorrect conclusions/bad decisions