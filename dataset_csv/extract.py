# import pandas as pd

# # 读取原始CSV文件
# input_file = 'tcga_brca_all_clean_copy.csv'
# df = pd.read_csv(input_file)

# # 指定要提取的列名
# column_name = 'slide_id'  # 将"ColumnName"替换为你要提取的列的实际名称

# # 提取指定列并保存为新的CSV文件
# output_file = 'origin_slide.csv'  # 输出文件名，可以自定义
# selected_column = df[column_name]
# selected_column.to_csv(output_file, index=False)

# import pandas as pd

# # 读取第一个CSV文件，包含要根据的列
# file_with_column = '/home/jupyter-ljh/data/mydata/Patch-GCN-master/dataset_csv/slide.csv'  # 将"file_with_column.csv"替换为包含要根据的列的文件名
# column_name = 'slide_id'  # 将"ColumnName"替换为你要根据的列的名称

# df_column = pd.read_csv(file_with_column)

# # 读取第二个CSV文件，包含要保留的行
# file_to_keep_rows = '/home/jupyter-ljh/data/mydata/Patch-GCN-master/dataset_csv//tcga_brca_all_clean.csv'  # 将"file_to_keep_rows.csv"替换为包含要保留行的文件名

# df_to_keep_rows = pd.read_csv(file_to_keep_rows)

# # 根据指定列的值筛选要保留的行
# selected_rows = df_to_keep_rows[df_to_keep_rows[column_name].isin(df_column[column_name])]

# # 保存筛选后的行为新的CSV文件
# output_file = '/home/jupyter-ljh/data/mydata/Patch-GCN-master/dataset_csv//tcga_brca_all_clean.csv'  # 输出文件名，可以自定义
# selected_rows.to_csv(output_file, index=False)
import csv

input_filename = './tcga_brca_all_clean.csv'
output_filename = './case_id.csv'

case_ids = []  # List to store case_id values

# Read the input CSV file
with open(input_filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        case_id = row['case_id']  # Assuming 'case_id' is the column header
        case_ids.append(case_id)

# Write the case_ids to the output CSV file
with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['case_id'])  # Write the header
    for case_id in case_ids:
        writer.writerow([case_id])  # Write each case_id

