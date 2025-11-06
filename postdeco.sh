#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Nope."
    exit 1
fi

path=$1
target="./decompiled/${path}/net/minecraft/"

if [ ! -d "$target" ]; then
    echo "No files to remmap lul"
    echo "$target needed dir"
    exit 1
fi

if [ ! -f "./jars/${path}/mappings/methods.csv" ]; then
    echo "No methods.csv cannot remmap"
    exit 1
fi

tail -n +2 "./jars/${path}/mappings/methods.csv" | while IFS=, read -r searge name side desc; do
    if [ -n "$searge" ] && [ -n "$name" ]; then
        echo "Process $searge -> $name..."
        found_files=$(find "$target" -name "*.java" -type f -exec grep -l "\b$searge\b" {} +)

        if [ -n "$found_files" ]; then
            count=$(echo "$found_files" | wc -l)
            echo "  Found in $count file(s):"
            echo "$found_files" | sed 's/^/    /'
            
            echo "$found_files" | xargs sed -i "s/\b$searge\b/$name/g"
            echo "  ✓ Replacement completed"
        else
            echo "  ✗ Not found in any files"
        fi
        echo ""
    fi
done

if [ ! -f "./jars/${path}/mappings/fields.csv" ]; then
    echo "No fields.csv cannot remmap"
    exit 1
fi

tail -n +2 "./jars/${path}/mappings/fields.csv" | while IFS=, read -r searge name side desc; do
    if [ -n "$searge" ] && [ -n "$name" ]; then
        echo "Process $searge -> $name..."
        found_files=$(find "$target" -name "*.java" -type f -exec grep -l "\b$searge\b" {} +)

        if [ -n "$found_files" ]; then
            count=$(echo "$found_files" | wc -l)
            echo "  Found in $count file(s):"
            echo "$found_files" | sed 's/^/    /'
            
            echo "$found_files" | xargs sed -i "s/\b$searge\b/$name/g"
            echo "  ✓ Replacement completed"
        else
            echo "  ✗ Not found in any files"
        fi
        echo ""
    fi
done