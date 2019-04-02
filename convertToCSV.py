# ls *.xls > dataFiles.txt
# rm *.xls
# ls *.csv > csvDataFiles.txt

import pandas as pd

file_names = open('Data/dataFiles.txt', 'r') 

data_files = file_names.readlines()

for file in data_files:
    file_name = 'Data/' + file[:-1]
    data_xls = pd.read_excel(file_name, index_col=None)
    new_file_name = file_name[:-4] + '.csv'
    data_xls.to_csv(new_file_name, index=False)

file_names.close()