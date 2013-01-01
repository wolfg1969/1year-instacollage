#!/usr/bin/env python

import sys
import time

from instagram.client import InstagramAPI

def download_image_url(access_token, userid, count):

	api = InstagramAPI(access_token=access_token)

	current_timestamp = time.time()

	print 'current_timestamp =', current_timestamp

	f = open('meta.txt', 'w')

	recent_media, next = api.user_recent_media(user_id=userid, count=count)

	while len(recent_media) > 0:

		for media in recent_media:
			#print media
                        #print media.images['thumbnail'].url, media.id, media.filter, len(media.likes)
                        #f.write('%s,%s,%s,%d\n' % (media.images['thumbnail'].url, media.id, media.filter, len(media.likes)))
			f.write('%s,%s,%s\n' % (media.id, media.filter, media.likes))

		recent_media, next = api.user_recent_media(user_id=userid, count=count,
			max_id=recent_media[-1].id)

	f.close()


if __name__ == '__main__':

	userid = sys.argv[1]
	access_token = sys.argv[2]
	count = 5

	print 'user_id =', userid
	print 'acess_token =', access_token

	download_image_url(access_token, userid, count)
