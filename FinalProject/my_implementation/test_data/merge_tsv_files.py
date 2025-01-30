import pandas as pd

# Load the first TSV file
file1 = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\my_main-results.tsv'
df1 = pd.read_csv(file1, sep='\t')

# Load the second TSV file
file2 = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E.tsv'
df2 = pd.read_csv(file2, sep='\t')

# file3 = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-A-SVM-results.tsv'
# df3 = pd.read_csv(file3, sep='\t')

# file4 = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E-LR-results.tsv'
# df4 = pd.read_csv(file4, sep='\t')

# Merge the two DataFrames
# Here, you can specify how you want to merge the two files (e.g., based on common columns)
merged_df = pd.concat([df1, df2], ignore_index=True)

# Optional: if you want to merge based on a common column, use `merge()` instead:
# merged_df = pd.merge(df1, df2, on='Geneset', how='outer')

# Save the merged DataFrame to a new TSV file
merged_df.to_csv('D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\my_main-results.tsv', sep='\t', index=False)

# Print the merged DataFrame to verify
# print(merged_df)
