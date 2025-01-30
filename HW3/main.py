import pandas as pd

df = pd.read_csv("./GSE15852.top.table.tsv", sep="\t")

# print(len(df))
significant_genes = df.loc[(df['adj.P.Val'] < 0.001) & (df['logFC'].abs() > 1)]
# print(len(significant_genes))
significant_genes.to_csv("sig_genes.csv", index=False)
print(len(significant_genes))
# print(len(significant_genes))
# print(type(data["Gene.title"][0]))