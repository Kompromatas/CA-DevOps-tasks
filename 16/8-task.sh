#!/bin/bash

replace_word() {
    local FILE=$1
    local WORD1=$2
    local WORD2=$3
      
    sed -i.bak "s/\b${WORD1}\b/${WORD2}/g" "$FILE"

    # Print the updated YAML
    echo "Word '$WORD1' replaced with '$WORD2' in $FILE !!!!!"

    cat "$FILE"

    
}

replace_word $1 $2 $3