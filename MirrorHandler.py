import urllib.request, json, config, os

mirror = config.MIRROR_URL
version = None

def Download(url: str, path: str):
    urllib.request.urlretrieve(url=url, filename=path)

def DecompilerJars(versionData: json):
    Download(versionData["decompiler"]["CFR"],           "./jars/CFR.jar")
    Download(versionData["decompiler"]["SpecialSource"], "./jars/SpecialSource.jar")

    Download(versionData["decompiler"]["client"],        "./jars/client/client.jar")
    Download(versionData["decompiler"]["server"],        "./jars/server/server.jar")
    Download(versionData["decompiler"]["client"],        "./jars/client/client.jar")

def DownloadGradle(projectDir: dir, versionData: json):
    base = os.path.abspath(projectDir)
    Download(versionData["build"][".gitignore"],           os.path.join(base, ".gitignore"))
    Download(versionData["build"]["build.gradle.kts"],           os.path.join(base, "build.gradle.kts"))
    Download(versionData["build"]["gradle.properties"],          os.path.join(base, "gradle.properties"))
    Download(versionData["build"]["settings.gradle.kts"],        os.path.join(base, "settings.gradle.kts"))
    Download(versionData["build"]["gradle-wrapper.properties"],  os.path.join(base, "gradle", "wrapper", "gradle-wrapper.properties"))

def ParseInitedVersion(projectVersion: str):
    global version
    version = projectVersion
    return ParseVersion()

def ParseVersion():
    if len(version)>1:
        return data["version"][version]
    
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
            id = int(input(f"\nSELECT (0-{len(versions)-1}): "))
            if id < 0 or id > len(versions):
                print("Bruh..")
                pass
            select = versions[id]
            print(f"VERSION: {select}")
            break
        return data["version"][select]