import pandas as pd

csv_names = open('Data/csvDataFiles.txt', 'r')

data_files = csv_names.readlines()
master_column_names = []
all_dfs = []

for i, file in enumerate(data_files):
    file_name = 'Data/' + file[:-1]
    df = pd.read_csv(file_name, header = 3)
    df.columns = [x.replace("\n", '') for x in df.columns]
    if i == 0:
        master_column_names = df.columns
    df.columns = master_column_names
    all_dfs.append(df)

csv_names.close()

result = pd.concat(all_dfs)
result.to_csv('NYCRealEstateData.csv', index = None)