import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# from library.sb_utils import save_file

ski_data = pd.read_csv('./raw_data/ski_resort_data.csv')


missing = pd.concat([ski_data.isnull().sum(), 100 * ski_data.isnull().mean()], axis=1)
missing.columns=['count', '%']
missing.sort_values(by=___)