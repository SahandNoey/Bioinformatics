import os

base_path = '../data/labels'
gscs_paths = ['BeFree', 'DisGeNet', 'GOBP', 'GOBPtmp', 'GWAS', 'MGI']
rem_nets_paths = ['BioGRID', 'STRING-EXP']
del_nets_paths = ['GIANT-TN', 'STRING']
output_path = [f'/home/sahand/University/Bioinformatics/my_implementation/data/labels/{i}/idmap1.tsv' for i in gscs_paths]
# print(idmap_path)
count = 0
for g_p in gscs_paths:
    rem_set = set()
    for n_p in rem_nets_paths:
        path = os.path.join(base_path, g_p, n_p)
        rem_set.update([os.path.splitext(file)[0] for file in os.listdir(path) if file.endswith(".tsv")])
    # print(rem_set)
    
    del_set = set()
    for n_p in del_nets_paths:
        path = os.path.join(base_path, g_p, n_p)
        f_names = [os.path.splitext(file)[0] for file in os.listdir(path) if file.endswith(".tsv")]
        # print(f_names)
        for i in f_names:
            if i not in rem_set:
                del_set.add(i)
    # print(del_set)

    idmap_path = os.path.join(base_path, g_p, "idmap.tsv")
    # with open(idmap_path, "r") as 
    with open(idmap_path, "r") as infile, open(output_path[count], "w") as outfile:
        header = infile.readline()  # Read the header line
        outfile.write(header)  # Write the header to the output file

        for line in infile:
            # Split the line into columns
            columns = line.strip().split("\t")
            
            # Check if the Name column (index 1) is not in the set
            if columns[1] not in del_set:
                outfile.write(line)  # Write the line if it doesn't match

    os.replace(output_path[count], idmap_path)
    count += 1

# files_and_dirs = os.listdir()



# print(files_and_dirs)
