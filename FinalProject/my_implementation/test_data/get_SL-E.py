# import pandas as pd

# # Load the TSV file into a pandas DataFrame
# file_path = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E.tsv'  # Replace with your actual file path
# df = pd.read_csv(file_path, sep='\t')

# # Remove rows where Network is 'GIANT-TN' or 'STRING', or Geneset Collection is 'GOBPtmp'
# filtered_df = df[~df['Network'].isin(['GIANT-TN', 'STRING']) &
#                  (df['Geneset Collection'] != 'GOBPtmp')]


# # Optionally, save the filtered result to a new TSV file
# filtered_df.to_csv('D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E.tsv', sep='\t', index=False)

# import pandas as pd

# # Load the first TSV file (this file contains the Genesets to keep)

# file_path_1 = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\my_main-results.tsv'  # Replace with your actual file path
# df1 = pd.read_csv(file_path_1, sep='\t')

# # Load the second TSV file (this file needs to be filtered)
# file_path_2 = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E.tsv'  # Replace with your actual file path
# df2 = pd.read_csv(file_path_2, sep='\t')

# # Filter rows in the second DataFrame where 'Geneset' is in the first DataFrame's 'Geneset'
# filtered_df2 = df2[df2['Geneset'].isin(df1['Geneset'])]

# # Optionally, save the filtered result to a new TSV file
# filtered_df2.to_csv('D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E.tsv', sep='\t', index=False)

import pandas as pd

# Load the TSV file
file_path = 'D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E.tsv'  # Replace with your actual file path
df = pd.read_csv(file_path, sep='\t')

# Filter rows where 'Network' is not equal to 'InBioMap'
filtered_df = df[df['Network'] != 'InBioMap']

# Optionally, save the filtered result to a new TSV file
filtered_df.to_csv('D:\Projects\PythonProjects\Bioinformatics\FinalProject\my_implementation\my_results\SL-E.tsv', sep='\t', index=False)
