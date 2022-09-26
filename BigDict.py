## Group Exercise 04 - A big Dictionary

# Write a program that creates a nested dictionary that has a biological or biochemical background
# Each sub-dictionary should contain at least seven different entries
# At least one number and one list
# The Main dictionary should contain at least 8 to 10 different entries
# Let the user either display, manipulate or add an entry to your main dictionary
# All changes have to be viable and be seen by the user

import json

Proteins = {}
Proteins["PRDM1"] = {"Name":"PR domain zinc finger protein 1", "Synonyms":"BLIMP1", "Length":825, "Molecular function":["DNA-binding", "Methyltransferase", "Repressor", "Transferase"], "Biological process":["Adaptive immunity", "Immunity", "Innate immunity", "Transcription", "Transcription regulation"], "Ligand":["Metal-binding", "S-adenosyl-L-methionine", "Zinc"], "Location": "Chromosome 6", "Subcellular location":["Nucleus", "Cytoplasm"]}
Proteins["IRF1"] = {"Name":"Interferon regulatory factor 1", "Length":325, "Molecular function":["Activator", "DNA-binding", "Repressor"], "Biological process":["Antiviral defense", "Immunity", "Innate Immunity", "Transcription", "Transcription regulation"], "Location":"Chromosome 5", "Subcellular location":["Nucleus", "Cytoplasm"]}
Proteins["STAT1"] = {"Name":"Signal transducer and activator of transcription 1" , "Length":750, "Molecular function":["Activator", "DNA-binding"], "Biological process":["Antiviral defense", "Host-virus interaction", "Transcription", "Transcription regulation"], "Location":"Chromosome 2", "Subcellular location":["Cytoplasm", "Nucleus"]}
Proteins["MCM5"] = {"Name":"Minichromosome maintenance complex component 5", "Synonyms":"CDC46", "Length":734, "Molecular function":["DNA-binding", "Helicase", "Hydrolase"], "Biological process":["Cell cycle", "DNA replication"], "Ligand":["ATP-binding", "Nucleotide-binding"], "Location": "Chromosome 22", "Subcellular location":["Nucleus", "Chromosome", "Cytoplasm"]}
Proteins["ORC2"] = {"Name":"Origin recognition complex subunit 2", "Synonyms":"ORC2L", "Length":577, "Biological process":["DNA replication"], "Location":"Chromosome 2", "Subcellular location":["Nucleus"]}
Proteins["CDC6"] = {"Name":"Cell division control protein 6 homolog", "Synonyms":"CDC18L", "Length":560, "Biological Process":["Cell cycle", "Cell division", "DNA replication", "Mitosis"], "Ligand":["ATP-binding", "Nucleotide-binding"], "Location":"Chromosome 17", "Subcellular location":["Nucleus", "Cytoplasm"]}
Proteins["PSKH1"] = {"Name":"Serine/threonine-protein kinase H1", "Length":424, "Molecular function":["Kinase", "Serine/threonine-protein kinase", "Transferase"], "Ligand":["ATP-binding", "Nucleotide-binding"], "Location":"Chromosome 16", "Subcellular location":["Golgi apparatus", "Cytoplasm", "Nucleus", "Endoplasmic reticulum membrane", "Cell membrane"]}
Proteins["MAPK2"] = {"Name":"Mitogen-activated protein kinase 2", "Length":400, "Molecular function":["Kinase", "Serine/threonine-protein kinase", "Transferase"], "Biological process":["DNA damage"], "Ligand":["ATP-binding", "Nucleotide-binding"], "Location":"Chromosome 1", "Subcellular location":["Cytoplasm", "Nucleus"]}

print("Here is the Protein dictionary:")
tmp = json.dumps(Proteins, indent=4)
print(tmp)
while True:
    user_op = input("\nWhat action would you like to perform for the dictionary? \nChoose either search, add, delete or change.\nType q to exit the program.\n")
# Adding to the dictionary. Either a whole new protein or add a new key-value pair to an existing protein
    if user_op == "add":
        user_input = input("Do you want to add a whole new protein (new) or add information to an existing protein (add)?\n")
        if user_input == "new":
            print("Please provide the information of the protein you want to add.")
            prot_abbr = input("Abbreviation of the protein: ")
            if prot_abbr in Proteins:
                print(f"{prot_abbr} already exists in the dictionary! It will not be added to avoid errors.")
            else:
                prot_name = input("Full name: ")
                prot_synonym = input("Synonyms: ")
                prot_length = int(input("Length (Amino acids): "))
                prot_mol_function = input("Molecular Function: ").split(", ")
                prot_biol_process = input("Biological process: ").split(", ")
                prot_ligand = input("Ligand: ").split(", ")
                prot_location = int(input("Location (Chromosome): "))
                prot_subcell_location = input("Subcellular location").split(", ")
                Proteins[prot_abbr] = {"Name":prot_name, "Synonym":prot_synonym, "Length":prot_length, "Molecular function":prot_mol_function, "Biological process":prot_biol_process, "Ligand":prot_ligand, "Location":(f"Chromosome {prot_location}"), "Subcellular location":prot_subcell_location}

                tmp = json.dumps(Proteins[prot_abbr], indent=4)
                print(f"This is the new entry for {prot_abbr}: \n{tmp}")
        elif user_input == "add":
            print("Please provide the information you want to add. Choose a protein from the following list:")
            print(*list(Proteins.keys()), sep=', ')
            prot_abbr = input("Abbreviation of the protein: ")
            if prot_abbr in Proteins:
                prot_key = input("Key: ")
                prot_value = input("Value: ")
                if prot_value.isdigit():
                    prot_value = int(prot_value)
                Proteins[prot_abbr][prot_key] = prot_value

                tmp = json.dumps(Proteins[prot_abbr], indent=4)
                print(f"This is the updated entry for {prot_abbr}: \n{tmp}")
            else:
                print(f"{prot_abbr} was not found in the dictionary!")
        else:
            print("Invalid Input")
# Deleting an entry. Asks the user for the abbreviation of the protein, which should be deleted.
    elif user_op == "delete":
        print("Which protein do you want to delete? Choose a protein from the following list:")
        print(*list(Proteins.keys()), sep=', ')
        prot_abbr= input("Abbreviation of the protein: ")
        if prot_abbr in Proteins:
            del Proteins[prot_abbr]

            tmp = json.dumps(Proteins, indent=4)
            print(f"This is the new dictionary: \n{tmp}")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
# Changing entries. Can only change values and not keys.
    elif user_op == "change":
        print("Which protein do you want to change? Choose from the following list:")
        print(*list(Proteins.keys()), sep=', ')
        prot_abbr = input("Abbreviation of the protein: ")
        if prot_abbr in Proteins:
            print("Choose from the following list, which part you want to change:")
            print(*list(Proteins[prot_abbr].keys()), sep=', ')
            prot_key = input()
            if prot_key in list(Proteins[prot_abbr].keys()):
                prot_value = input("New information: ")
                if prot_value.isdigit():
                    prot_value = int(prot_value)
                Proteins[prot_abbr][prot_key] = prot_value

                tmp = json.dumps(Proteins, indent=4)
                print(f"This is the new dictionary: \n{tmp}")
            else:
                print(f"{prot_key} is no available key in {prot_abbr}.")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
# Exit the program
    elif user_op == "q":
        exit()
# Search for a protein
    elif user_op == "search":
        prot_abbr = input("Which protein are you looking for? \nAbbreviation: ")
        if prot_abbr in Proteins:
            tmp = json.dumps(Proteins[prot_abbr], indent=4)
            print(f"Here is the entry for {prot_abbr}: \n{tmp}")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
# Invalid input if none of the above are true
    else:
        print("Invalid Input")
