1year-instacollage
==================

create a collage with my instagram photos last year

```
$ sudo easy_install python-instagram
$ python get_access_token.py
$ python meta.py user_id access_token
$ mkdir -p images/thumbnails
$ sh download.sh meta.txt thumbnails
$ mkdir images/2012
$ brew install pil
$ python collage.py images/2012 images/collage2012.jpg 8

$ awk -F\[  '{print $2;}' meta.txt | tr \] ' ' | sed  -e 's/User: //g' | sed -e 's/, / /g' > likes.txt
$  scripts/scald.rb --local Count.scala --input likes.txt --output likes.tsv

$ tail -10 filter.tsv | sort -k 2,2 -n | tail -r
```
