def convert_fasta_to_string(fasta_file):
    with open(fasta_file, "r") as f:
        lines = f.readlines()
    return "".join([line.replace("\n", "") for line in lines[1:]])