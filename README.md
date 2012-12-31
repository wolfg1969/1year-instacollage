1year-instacollage
==================

create a collage with my instagram photos last year

```
sudo easy_install python-instagram
$ python meta.py user_id access_token
$ mkdir -p images/thumbnails
$ sh download.sh meta.txt thumbnails
$ mkdir images/2012
$ python collage.py images/2012 images/collage2012.jpg
```