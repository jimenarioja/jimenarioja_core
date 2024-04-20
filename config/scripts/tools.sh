pretty_display() {
    local text="$1"
    local separator="$2"
    local line_length=$(($(tput cols) - 1))

    local pad_length=$(( (line_length - ${#text}) / 2 ))

    local padding=""
    for ((i=0; i<$pad_length; i++)); do
        padding+="$separator"
    done

    local output="$padding$text$padding"

    local line_separator=""
    for ((i=0; i<$line_length; i++)); do
        line_separator+="$separator"
    done

    echo "$line_separator"
    echo "$output"
    echo "$line_separator"
}
