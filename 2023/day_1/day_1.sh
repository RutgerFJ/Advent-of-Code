#!/bin/bash

part_one() {
    sum=0

    while read -r line; do
        line_digits=$(echo "$line" | tr -cd '[:digit:]')
        line_value="${line_digits:0:1}${line_digits: -1}"
        sum=$(($sum + $line_value))
    done < "input.txt"

    echo "$sum"
}

part_two() {
    sum=0

    while read -r line; do
        line_digits=$(echo "$line" |
            sed '
                s/one/one1one/g;
                s/two/two2two/g;
                s/three/three3three/g;
                s/four/four4four/g;
                s/five/five5five/g;
                s/six/six6six/g;
                s/seven/seven7seven/g;
                s/eight/eight8eight/g;
                s/nine/nine9nine/g' |
            tr -cd '[1-9]')
        line_value=$(echo "${line_digits:0:1}${line_digits: -1}")
        sum=$(($sum + $line_value))
    done < "input.txt"
    echo "$sum"
}

main() {
    echo "$(part_one)"
    echo "$(part_two)"
}

main
