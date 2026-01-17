import urllib.request, json, config

mirror = config.MIRROR_URL

def Download(url: str, path: str):
    urllib.request.urlretrieve(url=url, filename=path)

def DecompilerJars(versionData: json):
    Download(versionData["decompiler"]["CFR"],           "./jars/CFR.jar")
    Download(versionData["decompiler"]["SpecialSource"], "./jars/SpecialSource.jar")

    Download(versionData["decompiler"]["client"],        "./jars/client/client.jar")
    Download(versionData["decompiler"]["server"],        "./jars/server/server.jar")

def ParseVersion():
    with urllib.request.urlopen(mirror) as url:
        data = json.loads(url.read().decode())
        versions = list(data["version"].keys())

        if not versions: 
            print("No versions avalible in mirror") 
            exit()
        
        for i, version in enumerate(versions, 0):
            print(f"[{i}] --->>> {version}")
        
        global select
        select = None

        while True:
            id = int(input(f"\nSELECT (0-{len(versions)}): "))
            if id < 0 or id > len(versions):
                print("Bruh..")
                pass
            select = versions[id]
            print(f"VERSION: {select}")
            break
        return data["version"][select]