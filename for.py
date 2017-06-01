import os
import requests

'''
f = []
dirlist = os.listdir('/root/python/image')
for filename in dirlist:
	f.append(filename)
print f
'''
for filename in os.listdir('/root/python/image'):
	print (filename)	
url_upload = 'http://v0.api.upyun.com/test20160418/%s' % filename

print (url_upload)
