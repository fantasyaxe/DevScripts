#!/bin/bash

./pre-init.sh

while true; do
    read -p "
    What u have?
    1 - Client only
    2 - Server only
    3 - All (default)
    Enter [1-3]: " JARS

    case "${JARS:-3}" in
        1) jars=("client"); break ;;
        2) jars=("server"); break ;;
        3) jars=("client" "server"); break ;;
        *) echo "Bruh" ;;
    esac
done

for jar in "${jars[@]}"; do
    ./deobf.sh "$jar"
    ./decompile.sh "$jar"
done

# Пути
# client -> jars/client/client.jar
# server -> jars/server/server.jar
# CFR -> jars
# SpecialSource -> jars

# Деобфусцированный jar -> jars/(client|server)/deobfuscated/(client|server).jar
# Декомпилированный jar -> decompiled/(client|server)/

# Для деобфускации
# java -jar SpecialSource.jar --in-jar {jar}.jar --out-jar .\deobf\{jar}.jar --srg-in .\conf\joined.srg
# sh deobf.sh

# Для декомпиляции
# java -jar CFR.jar {jar}.jar --outputdir decompiled/
# sh decompile.sh