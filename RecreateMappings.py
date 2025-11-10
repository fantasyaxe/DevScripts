import csv

final_file = "mappings/mapping.csv"

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

    util_list = {}
    for mapping in process_mappings:
        util_list[mapping['obfuscated']] = mapping['deobfuscated']

    for obf in util_list:
        deobf = util_list[obf]
        while deobf in util_list and deobf != util_list[deobf]:
            deobf = util_list[deobf]
        util_list[obf] = deobf

    process_mappings = [{'obfuscated': obf, 'deobfuscated': deobf} for obf, deobf in util_list.items()]
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