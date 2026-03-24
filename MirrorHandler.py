import urllib.request, json, config, os

def load_mirror():
    with urllib.request.urlopen(config.MIRROR_URL) as url:
        return json.loads(url.read().decode())

def Download(url: str, path: str):
    urllib.request.urlretrieve(url=url, filename=path)

def DecompilerJars(versionData: json):
    Download(versionData["decompiler"]["CFR"],           "./jars/CFR.jar")
    Download(versionData["decompiler"]["SpecialSource"], "./jars/SpecialSource.jar")

    Download(versionData["decompiler"]["client"],        "./jars/client/client.jar")
    Download(versionData["decompiler"]["server"],        "./jars/server/server.jar")

def DownloadGradle(projectDir: str, versionData: dict):
    base = os.path.abspath(projectDir)
    Download(versionData["build"][".gitignore"],           os.path.join(base, ".gitignore"))
    Download(versionData["build"]["build.gradle.kts"],     os.path.join(base, "build.gradle.kts"))
    Download(versionData["build"]["gradle.properties"],    os.path.join(base, "gradle.properties"))
    Download(versionData["build"]["settings.gradle.kts"],  os.path.join(base, "settings.gradle.kts"))
    Download(versionData["build"]["gradle-wrapper.properties"], os.path.join(base, "gradle", "wrapper", "gradle-wrapper.properties"))

def load_version(version: str =""):
    data = load_mirror()
    versions = list(data["version"].keys())
    if not versions:
        print("Versions list is empty")
        exit()
    if version and version in versions:
        return data["version"][version], version
    for i, v in enumerate(versions):
        print(f"[{i}] --->>> {v}")
    while True:
        try:
            idx = int(input(f"\nSELECT (0-{len(versions)-1}): "))
            if 0 <= idx < len(versions): return data["version"][versions[idx]], versions[idx]
        except ValueError: pass
        print("Bruh..")