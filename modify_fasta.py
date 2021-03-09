def replace_char(char, file_path):
    """
    replaces all occurences of the given char in the file with a space
    """
    lines = []

    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = list(map(lambda i: i.replace(char, ' '), lines))

    with open(file_path, 'w') as f:
        for line in lines:
            f.write(line)

char = '|'
replace_char(char, "drug_target_data/target_structures/targets.fasta")
replace_char(char, "drug_target_data/target_structures/carriers.fasta")
replace_char(char, "drug_target_data/target_structures/transporters.fasta")
replace_char(char, "drug_target_data/target_structures/enzymes.fasta")