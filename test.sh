val="$(sensors)"
# $emp = "$val" | awk '/Tdie:+/ {gsub(/[^0-9.]/,"",$2)}'
echo "$val" | awk '/Tdie:+/ {gsub(/[^0-9.]/,"",$2)} END {print $2}' 
