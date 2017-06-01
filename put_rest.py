import datetime
import hashlib
import os
import requests
import base64

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
bucket = 'test20160418'
operator = 'admin'
METHOD = 'PUT'
PASSWORD = 'weihao123'
pd = hashlib.md5(PASSWORD.encode('utf-8'))
pd1 = pd.hexdigest()
print(pd1)

p = operator + ':' + PASSWORD
pas = base64.b64encode(p)


length = str(os.path.getsize('/root/python/psb.jpg'))
url = 'http://v0.api.upyun.com/test20160418/3.jpg'
files = {'file': open('/root/python/psb.jpg','rb')}
headers = {
    'Authorization': 'Basic ' + pas,
    'Date': DATE,
    'Content-Length':length,
    }
res = requests.request('PUT',url,data = files ,headers = headers)
print(res.status_code)
print(DATE)
print(pd1)
#print(qm1)
print (length)
print (pas)
print (p)
