#!/bin/bash

replace_word() {
    local FILE=$1
    local WORD1=$2
    local WORD2=$3

    # Replace word using yq
    #yq eval 'walk(if type == "string" then gsub("'"$WORD1"'"; "'"$WORD2"'") else . end)' "$FILE" > temp.yaml && mv temp.yaml "$FILE"
    #yq eval '(.. | select(tag == "!!str") |= sub("'"$WORD1"'"; "'"$WORD2"'"))' "$FILE" > temp.yaml && mv temp.yaml "$FILE"
    #yq eval "(.. | select(tag == \"!!str\") |= sub(\"$WORD1\"; \"$WORD2\"))" "$FILE" > temp.yaml && mv temp.yaml "$FILE"
    #yq eval "(.[] | .. | select(tag == \"!!str\") |= sub(\"$TARGET_WORD\"; \"$REPLACEMENT_WORD\"))" "$FILE" > temp.yaml && mv temp.yaml "$FILE"
    sed -i.bak "s/\b${WORD1}\b/${WORD2}/g" "$FILE"


    # Print the updated YAML
    echo "Word '$WORD1' replaced with '$WORD2' in $FILE !!!!!"

    cat "$FILE"

    
}

replace_word $1 $2 $3