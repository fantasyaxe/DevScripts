import os
import subprocess as sub
import MirrorHandler as mirror

global editions
editions = []

def DownloadSources():
    data = mirror.ParseVersion()
    mirror.DecompilerJars(data)

def SelectEdition():
    while True:
        print("""
              1 - Server
              2 - Client
              3 - All
              """)
        id = int(input(f"\nSelect game edition: "))
        if id < 1 or id > 3:
            print("Bruh..")
            pass
        if id == 1: editions.append("server")
        if id == 2: editions.append("client")
        if id == 3: editions.extend(["server", "client"])
        print(f"EDITIONS: {editions}")
        break

def CreateStructure():
    os.makedirs("./patches/client", exist_ok=True)
    os.makedirs("./patches/server", exist_ok=True)
    os.makedirs("./jars/client",    exist_ok=True)
    os.makedirs("./jars/server",    exist_ok=True)
    os.makedirs("./src/client",     exist_ok=True)
    os.makedirs("./src/server",     exist_ok=True)
    os.makedirs("./mappings",       exist_ok=True)
    os.makedirs("./deobfuscated",   exist_ok=True)
    os.makedirs("./decompiled",     exist_ok=True)

if __name__ == "__main__":
    SelectEdition()
    CreateStructure()
    DownloadSources()
    
    sub.run(["python", "RecreateMappings.py"])
    for edition in editions:
        sub.run(["java", "-jar", "./jars/SpecialSource.jar", "--in-jar", 
                 f"./jars/{edition}/{edition}.jar", "--out-jar", 
                 f"./deobfuscated/{edition}.jar", "--srg-in", "./mappings/packaged.srg"])
        sub.run(["java", "-jar", "./jars/CFR.jar", f"./deobfuscated/{edition}.jar", "--outputdir", f"./decompiled/{edition}"])
        sub.run(["python", "PostDecompile.py", edition])
    