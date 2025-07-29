import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(r)
# >> <Response [200]>

print(dir(r))
# >> 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

#print(help(r))
print(r.text)

img_url = 'https://picsum.photos/200/300'
r = requests.get(img_url)
print(r.content)        # bytes
# >> xc8\xd1i\xdd\x8c\xc7\xff\x00\x86\x87\x02T\xca\x13\x99\xf5)\xcfa|\xe0\x94\x95\xf6 \xb7\x06\x9b

## Save image
with open('./data/image.png', 'wb') as f:
    f.write(r.content)

## Status code of webpage
print(r.status_code)
# >> 200

## for any less than 400 response
print(r.ok)
# >> True

print(r.headers)
''' 
####################### OUTPUT ##########################
{'Connection': 'keep-alive', 'Content-Length': '4606', 
'Server': 'nginx', 'Content-Type': 'image/jpeg', 'Cache-Control': 'public,
max-age=2592000, stale-while-revalidate=60, stale-if-error=43200, 
immutable', 'Content-Disposition': 'inline; filename="794-200x300.jpg"', 
'Picsum-Id': '794', 'Timing-Allow-Origin': '*', 'Accept-Ranges': 'bytes', 
'Age': '1254870', 'Date': 'Tue, 29 Jul 2025 14:02:47 GMT', 
'Via': '1.1 varnish', 'X-Served-By': 'cache-maa10246-MAA', 
'X-Cache': 'HIT', 'X-Cache-Hits': '0', 'X-Timer': 'S1753797768.618871,VS0,VE1', 
'Vary': 'Origin'}
##########################################################
'''

# payload -- data you send to the server as part of your request.
# for get() - query params
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbingo.org/get', params=payload)

#print(r.text)

print(r.url)
# >> https://httpbingo.org/get?page=2&count=25

# for post() - request param
payload = {'username': 'shreya', 'password': 'testing'}
r = requests.post('https://httpbingo.org/post', data=payload)
print(r.text)
''' 
####################### OUTPUT ##########################
"url": "https://httpbingo.org/post",
"data": "username=shreya&password=testing",
"files": {},
"form": {
    "password": [
      "testing"
    ],
    "username": [
      "shreya"
    ]
  },
##########################################################
'''

r_dict = r.json()
print(r_dict)
# >> {'args': {}, 'headers': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate'], 'Content-Length': ['32'], 'Content-Type': ['application/x-www-form-urlencoded'], 'Host': ['httpbingo.org'],

print(r_dict['form'])
# >> {'password': ['testing'], 'username': ['shreya']}


# Testing authentication with username and password
r = requests.get('https://httpbin.org/basic-auth/shreya/test', auth=('shreya', 'test'))
print(r)
# >> <Response [200]>
print(r.text)
''' 
####################### OUTPUT ##########################
{
  "authenticated": true,
  "user": "shreya"
}
##########################################################
'''

# wrong auths
r = requests.get('https://httpbin.org/basic-auth/shreya/test', auth=('shreyaparse', 'test'))

print(r.text)   # no output, blank line
print(r)
# >> <Response [401]>

# Delay in loading server
r= requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)
# >> <Response [200]>

# if it takes 6 sec to load server , it must raise session time out
r= requests.get('https://httpbin.org/delay/6', timeout=3)
print(r)
''' 
####################### OUTPUT ##########################
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=3)
##########################################################
'''
