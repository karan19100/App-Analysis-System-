import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# <---------------------------   Loading / Reading the csv file  --------------------------->

df = pd.read_csv(r'C:\Users\USer\Desktop\tp\kaggle-google-apps-master\googleplaystore.csv')
print(df.head(10))


# <--------------------------- creating  a profile overview report on dataset --------------------------->

from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='report.html')


# an report is been created on dataset name as report.html you can see in my repository.








