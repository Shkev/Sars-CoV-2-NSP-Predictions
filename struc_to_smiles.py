import pandas as pd

"""
extracting approved drugs from DrugBank data and writing the drug SMILES to a separate file
"""

drugs_df = pd.read_csv('./drug_target_data/drug_structures/drug_structure_links.csv')
# only using approved drugs
drugs_df = drugs_df.loc[drugs_df['Drug Groups'].str.contains('approved')].dropna(subset=['SMILES'])

with open('./drug_target_data/drug_structures/approved_drug.smi', 'w', encoding='utf-8') as f:
    for i, r in drugs_df.iterrows():
        f.write(r['SMILES'] + '\t' + r['DrugBank ID'] + ";" + r['Name'] + '\n')
