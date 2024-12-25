import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '../csv_files/hospital_test.csv')
df = pd.read_csv(file_path)

df.to_csv(sys.stdout)