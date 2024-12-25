import pandas as pd
import sys

df = pd.read_csv('./../csv_files/hospital_change_admitting_service_class.csv')

df.to_csv(sys.stdout)