#!/usr/bin/python
#coding:UTF-8

import datetime
import hashlib
import requests
import urllib


bucket = 'test20160418'
operator = 'admin'
password = 'weihao123'


GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
url = raw_input('please input your url:')

pd = hashlib.md5(password.encode('utf-8'))
pd1 = pd.hexdigest()

sign = url + '&' + bucket + '&' + DATE + '&' + pd1
sig = hashlib.md5(sign.encode('utf-8'))
sig1 = sig.hexdigest()

payload =urllib.urlencode({'purge':url})

headers = {
    'Authorization': 'UpYun ' + bucket + ':' + operator + ':' + sig1,
    'Date': DATE,
    "Content-Type": "application/x-www-form-urlencoded",
    }
conn = requests.post('http://purge.upyun.com/purge/',payload,headers=headers)

print conn.text
print conn.status_code

