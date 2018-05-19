import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data/wineQuality/winequality-red.csv"
all_data = pd.read_csv(file_path,sep=';')


feats = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']
target = ['quality']

unique_count = all_data.groupby(by=['quality']).size().reset_index()
unique_count.rename(columns={0:'count'},inplace=True)

cnt_srs =all_data['quality'].value_counts()
plt.figure(figsize=(12,6))
sns.barplot(cnt_srs.index, cnt_srs.values, alpha=0.8)
# plt.xticks(rotation='vertical')
# plt.xlabel('Month of transaction', fontsize=12)
# plt.ylabel('Number of Occurrences', fontsize=12)
plt.show()