from itertools import islice

# Input and output file paths
input_file_path = "/home/sahand/University/Bioinformatics/GenePlexus-master/data/embeddings/BioGRID.emd"  # Replace with your .edg file path
# output_file_path = "STRING-EXP-first10000.edg"  # Replace with your desired output file path

# Read the first 100 rows and save them to another file
with open(input_file_path, 'r') as infile:
    for line in islice(infile, 5):  # Reads and writes the first 10000 lines
        print(len(line.split(" ")))

# print(f"The first 100 rows have been saved to {output_file_path}")
