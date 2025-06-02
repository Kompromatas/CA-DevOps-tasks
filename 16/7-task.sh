#!/bin/bash

# Variables
FILE="3-task.json"  # Your JSON file
WORD1="cooking"
WORD2="cooding"

# Replace word using jq
jq --arg target "$WORD1" --arg replace "$WORD2" '
    walk(if type == "string" then gsub($target; $replace) else . end)
' "$FILE" > temp.json && mv temp.json "$FILE"

echo "Word '$WORD1' replaced with '$WORD2' in $FILE !!!!!"
jq . "$FILE"  # Display the updated JSON file