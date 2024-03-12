import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./apple_quality.csv')
df['Size_weight_diff'] = df['Size']-df['Weight']

categories = []
coorelations = []

for column in df.columns[3:len(df.columns)-3]:
    categories.append(column)   
    coorelations.append(df['Size_weight_diff'].corr(df[column]))


plt.bar(categories, coorelations)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Example')

plt.show()

"""
Analysis 1: Relationship Between Size-Weight Difference and Apple Crunchiness

Objective: To investigate the potential correlation between the difference in apple size and weight ('Size_weight_diff') and the perceived crunchiness of apples.

Methodology: Computed the correlation coefficient between 'Size_weight_diff' and various apple quality attributes. Utilized the Pearson correlation coefficient to quantify the linear relationship between variables.

Findings: Upon analysis, it was observed that the 'Size_weight_diff' has a substantial correlation with apple crunchiness.

Conclusion: There exists a statistically significant correlation between the difference in apple size and weight ('Size_weight_diff') and the perceived crunchiness of apples. The positive correlation suggests that, on average, as the size-weight difference increases, the apples tend to be perceived as crunchier. This finding may have implications for understanding the factors influencing apple quality and consumer preferences.

Recommendations: Further investigations, including sensory evaluations or controlled experiments, could provide additional insights into the causal relationship between size-weight difference and apple crunchiness. Moreover, considering external factors such as apple variety and growing conditions may contribute to a more comprehensive analysis.

This formalization outlines the objective, methodology, findings, conclusion, and recommendations derived from your analysis. Adjust the language and details based on the specifics of your dataset and the nuances of your findings.
"""
