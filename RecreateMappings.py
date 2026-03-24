#!/usr/bin/env python3
import csv

final_file = "mappings/mappings.csv"

def wroteFile(fileName, list):
    with open(fileName, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['obfuscated', 'deobfuscated'])
        writer.writeheader()
        writer.writerows(list)

def process():

    process_mappings = []
    starred_mappings = []

    with open("mappings/raw.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                obf, deobf = row[0], row[1]
                if obf.startswith('func') or obf.startswith('field'):
                    process_mappings.append({
                        'obfuscated': obf,
                        'deobfuscated': deobf
                    })
                if obf == "*":
                    starred_mappings.append({
                        'obfuscated': obf,
                        'deobfuscated': deobf
                    })

    id_replacements = {}
    for mapping in process_mappings:
        if mapping['deobfuscated'].startswith('field_') or mapping['deobfuscated'].startswith('func_'):
            id_replacements[mapping['obfuscated']] = mapping['deobfuscated']

    final_mappings = {}
    for mapping in process_mappings:
        obf = mapping['obfuscated']
        deobf = mapping['deobfuscated']
        if not (deobf.startswith('field_') or deobf.startswith('func_')):
            final_obf = id_replacements.get(obf, obf)
            final_mappings[final_obf] = deobf

    process_mappings = [{'obfuscated': obf, 'deobfuscated': deobf} for obf, deobf in final_mappings.items()]

    lolIDKwhatNameGiveForIt = {mapping['obfuscated'] for mapping in process_mappings}
    starred_mappings = [mapping for mapping in starred_mappings 
                       if mapping['deobfuscated'] not in lolIDKwhatNameGiveForIt]

    wroteFile("mappings/unknown.csv", starred_mappings)
    wroteFile(final_file, process_mappings)

    print(f"Total founded mappings: {len(process_mappings)}.\nSaved as {final_file}")
    print(f"Total not founded mappings: {len(starred_mappings)}. \nSaved as unknown.csv")

def compareMappings():

    filesToCompare = [
        "mappings/newids.csv",
        "mappings/methods.csv",
        "mappings/fields.csv"
    ]

    all_mappings = []

    for fi1e in filesToCompare:
        with open(fi1e, 'r', encoding='utf-8') as f:
            f_line = f.readline().strip()
            if f_line == "client,server,newid":
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        old_id, unused, new_id = row[0], row[1], row[2]
                        all_mappings.append({
                            'obfuscated': old_id,
                            'deobfuscated': new_id
                        })                
                print(f"{fi1e} done.")
            elif f_line == "searge,name,side,desc":
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        obf, deobf = row[0], row[1]
                        all_mappings.append({
                            'obfuscated': obf,
                            'deobfuscated': deobf
                        })    
                print(f"{fi1e} done.")
            else:   print(f"Unknown format: {fi1e}")
    wroteFile("mappings/raw.csv", all_mappings)

# Хз, что писать
if __name__ == "__main__":
    compareMappings()
    process()