#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Nope."
    exit 1
fi

path=$1
mkdir -p "deobfuscated"
java -jar ./jars/SpecialSource.jar --in-jar ./jars/${path}/${path}.jar --out-jar "./deobfuscated/${path}.jar" --srg-in ./jars/${path}/mappings/mappings.srg
#java -jar ./jars/SpecialSource.jar --in-jar ./deobfuscated/pre-${path}.jar --out-jar "./deobfuscated/${path}.jar" --srg-in ./jars/${path}/mappings/packaged.srg

# Для деобфускации
# java -jar SpecialSource.jar --in-jar {jar}.jar --out-jar .\deobf\{jar}.jar --srg-in .\conf\joined.srg
# sh deobf.sh