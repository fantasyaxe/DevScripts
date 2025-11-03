#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Nope."
    exit 1
fi

path=$1
mkdir -p "decompiled/${path}"
java -jar ./jars/CFR.jar "./deobfuscated/${path}.jar" --outputdir "./decompiled/${path}"

# Для декомпиляции
# java -jar CFR.jar {jar}.jar --outputdir decompiled/
# sh decompile.sh