#!/usr/bin/env python3
import os, sys, csv, threading
from concurrent.futures import ThreadPoolExecutor

pools = 4
used_mappings = []
lock = threading.Lock()

def replaceInFile(file, replace):
    with lock: print(f"Processing {file}..")
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    o_data = data
    for obfuscated, deobfuscated in replace:
        if obfuscated in data:
            with lock: 
                if deobfuscated in used_mappings == None:
                    used_mappings.append(obfuscated, deobfuscated)
            data = data.replace(obfuscated, deobfuscated)
            with lock: print(f"Replaced {obfuscated} -> {deobfuscated}\nIn {file}")
    if data != o_data:
        with open(file, "w", encoding="utf-8") as f:
            f.write(data)

def foundFiles(directory, replace):
    threads = []
    files = []
    for root, unused, filez in os.walk(directory):
        for file in filez:
            files.append(os.path.join(root, file))
    with ThreadPoolExecutor(max_workers=pools) as threadManager:
        for file in files:
            thread = threadManager.submit(replaceInFile, file, replace)
            threads.append(thread)
        for thread in threads:
            thread.result()


def process(version):
    directory = f"decompiled/{version}/net/minecraft/"
    mappings_file = "mappings/mappings.csv"

    if version is None:
        print("Invoke it with client|server arg!")
        return
    if not os.path.exists(directory):
        print("No files for remap.")
        print(f"{directory} needed directory")
        return
    if not os.path.exists(mappings_file):
        print("Cannot found mappings.")
        print(f"Try RecreateMappings.py first")
        return
    print("Process...")

    mappings = []
    with open("mappings/mappings.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                mappings.append((row[0], row[1]))
    foundFiles(f"decompiled/{version}/net/minecraft/", mappings)
    saveUnused(mappings)

def saveUnused(mappings):
    unused = [m for m in mappings if m not in used_mappings]
    with open("mappings/unused.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        for obfuscated, deobfuscated in unused:
            writer.writerow([obfuscated, deobfuscated])

# Бябябя Бебебе Бубубу

if __name__ == "__main__":
    process(sys.argv[1])