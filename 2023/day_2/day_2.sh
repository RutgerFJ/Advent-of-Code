#!/bin/bash

part_one() {
    sum=0

    while read -r line; do
        game_num=$(echo "$line" | awk '{print substr($2, 1, (length($2)-1))}')
	over_thresh=$(echo "$line"  | egrep -o '[1-9]([3-9] red|[4-9] green|[5-9] blue)')
	if [[ ${#over_thresh} -lt 1 ]]; then
            sum=$(($sum + $game_num))
	fi
    done < "input.txt";

    echo "$sum"
}

part_two() {
    sum=0

    while read -r line; do
        line_value=$(echo "$line" | sed -E 's/Game [0-9]://' | tr -d ';,' | awk '{
            for (i = 1; i <= NF; i += 2) {
                number=$i;
                color=$(i+1);
                if (number > max[color]) {
                    max[color]=number;
                }
            }
        }
        END {
            print max["blue"] * max["red"] * max["green"];
            }'
        )
        sum=$(($sum + $line_value))
    done < "input.txt";

    echo "$sum"
}

main() {
    echo "$(part_one)"
    echo "$(part_two)"
}

main
