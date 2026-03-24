#!/usr/bin/env python3
import os, shutil
import MirrorHandler as mirror

def CreateStructure(projectDir: str):
    projectPath = os.path.abspath(projectDir)
    os.makedirs(projectPath, exist_ok=True)
    os.makedirs(os.path.join(projectPath, ".scripts"),          exist_ok=True)
    os.makedirs(os.path.join(projectPath, "gradle", "wrapper"), exist_ok=True)

    os.makedirs(os.path.join(projectPath, "patches", "server"), exist_ok=True)
    os.makedirs(os.path.join(projectPath, "patches", "client"), exist_ok=True)
    os.makedirs(os.path.join(projectPath, "patches", "api"),    exist_ok=True)

def MoveSources(srcDir: str, projectDir: str):
    src = os.path.abspath(srcDir)
    dst = os.path.abspath(os.path.join(projectDir, "src", "main", "java"))
    
    os.makedirs(dst, exist_ok=True)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        shutil.move(s, d)

def DownloadGradle(projectDir: dir, projectVersion: str):
    data = mirror.ParseInitedVersion(projectVersion=projectVersion)
    mirror.DownloadGradle(projectDir, data)

def init(srcDir: dir, projectDir: dir, projectVersion: str):
    CreateStructure(projectDir=projectDir)
    DownloadGradle(projectDir=projectDir, projectVersion=projectVersion)
    MoveSources(srcDir, projectDir)
    