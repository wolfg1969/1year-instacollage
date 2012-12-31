#!/bin/sh
# download.sh url.txt dir
IFS=,
while read -r url id filter count
do
    echo $id
    wget -q $url -O images/$2/$id.jpg
done < $1
