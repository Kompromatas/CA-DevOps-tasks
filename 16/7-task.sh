#!/bin/bash

# Variables
FILE="3-task.json"  # Your JSON file
WORD1="cooking"
WORD="cooding"

# Replace word using jq
jq --arg target "$WORD1" --arg replace "$WORD2" '
    walk(if type == "string" then gsub($target; $replace) else . end)
' "$FILE" > temp.json && mv temp.json "$FILE"

echo "✅ '$WORD1' replaced with '$WORD2' in $FILE"