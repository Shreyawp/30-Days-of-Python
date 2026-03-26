### Djoser with DRF

Ref: [Djoser Readme](https://github.com/sunscrapers/djoser?tab=readme-ov-file#djoser)
[Djoser Doc](https://djoser.readthedocs.io/en/latest/index.html)
[DRF TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

Djoser - is REST API implementation of Django's Authentication system
       - usaually used with React/React Native/Vue.js as Frontend 
       - it provides out-of-box endpoints for things like login, logout, registering, password reset and account activation


Step 1: Install Djoser and [`django-cors-headers`](http://pypi.org/project/django-cors-headers/) package, used to send cross origi requests from React frontend to Django backened, in venv
>> pip install djoser
>> pip install django-cors-headers

Step 2: In settings.py, add following to INSTALLED_APPS as seen in [Djoser's getting started configurations](https://djoser.readthedocs.io/en/latest/getting_started.html#configuration)
```
'rest_framework.authtoken',
'djoser',
'corsheaders',
```

Also, `"corsheaders.middleware.CorsMiddleware",` in MIDDLEWARE
and paste this below
```
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
```

From [Authentication setting scheme](https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme), add following
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

Step 2: Run migrate on terminal
>> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, api, auth, authtoken, contenttypes, sessions, silk
Running migrations:
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
  Applying authtoken.0004_alter_tokenproxy_options... OK


Must Read Djoser [settings](https://djoser.readthedocs.io/en/latest/settings.html) and [serializers](https://djoser.readthedocs.io/en/latest/settings.html#serializers) in settings


Step 3: Add urlpatterns in mysite/urls.py and import re_path
` re_path(r'^auth/', include('djoser.urls')),
re_path(r'^auth/', include('djoser.urls.authtoken')),`

Step 4: Install VSCode extention "REST Client". 
        - This allows to send API or HTTP requests to backend (using api.http file) and can help inspect the response

Token Based Authentication has following available endpoints:
- /token/login/ 
- /token/logout/ 

Step 5: Send  following api request from api.http
`GET http://localhost:8000/auth/users/me/ HTTP/1.1`
![alt text](media/31_unauthorized_request.PNG)

To login using token authentication, send POST request as below
```
POST http://localhost:8000/auth/token/login/ HTTP/1.1
Content-Type: application/json

{
    "username": "admin",
    "password": "test"
}
```
![alt text](media/31_generate_auth_token.PNG)
From above POST response copy the auth_token.

Send following GET request with auth_token
```
GET http://localhost:8000/auth/users/me/ HTTP/1.1
Authorization: Token a34c4dd1771a76a3fed673b1fb4c5b050f3fd74a
```
![alt text](media/31_get_request_using_auth_token.PNG)

Now, goto SQLITE explorer and view authtoken_token TABLE, it has key(auth_token), created and user_id table headers.
![alt text](media/31_SQLite_auth_table.PNG)

DRF Auth Token package work is that it stores the tokens in DB and they are linked to the user
This means it has to run DB lookup every time a token comes into backend.

This different from JWT authentications, its called stateless authentication.
JWTs don't hit DB, that's because token is all that's needed to verify who is sending the request.
When using JWT tokens, we can save DB query per request.

Step 6: Send logout request
```
POST http://localhost:8000/auth/token/logout/ HTTP/1.1
Authorization: Token <token_id>
```
![alt text](media/31_logout_request.PNG)
Verify logout by sending another GET request from above


Now open the authtoken_token TABLE, will be empty.

JWT is most commonly used authentication with REACT or Vue.js
JSON Web Token Authentication has following available endpoints:
- /jwt/create/
- /jwt/refresh/
- /jwt/verify/ 


[Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

Step 1: Install JWT
>> pip install djangorestframework-simplejwt

Step 2: Add [JWT global settings](https://djoser.readthedocs.io/en/latest/authentication_backends.html#json-web-token-authentication)
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
    ..
}
```
after adding the above, not need to run migrate cmd unless using simplejwt blacklist app
and
```
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}
```

Step 3: add url from [Djoser JWT doc](https://djoser.readthedocs.io/en/latest/authentication_backends.html#urls-py)
`re_path(r'^auth/', include('djoser.urls.jwt')),`

Step 4: Testing for Simple JWT, Add new request in api.http and runserver 
```
POST http://localhost:8000/auth/jwt/create/ HTTP/1.1
Content-Type: application/json

{
    "username": "admin",
    "password": "test"
}

```

Send POST request and response has one refresh token n one access token
![alt text](media/31_JWT_request.PNG)

NOTE: access token is atteched to authorization header in order to prove to Django that user is authenticated to this token.
access token have small lifetime, they expire quickly and can exchange a refresh token to get new access token

Send below GET request:
```
GET http://localhost:8000/auth/users/me/ HTTP/1.1
Authorization: JWT <access_token>
```
Response is user details.
![alt text](media/31_JWT_get_request.PNG)

Test refresh endpoint:
```
POST http://localhost:8000/auth/jwt/refresh/ HTTP/1.1
Content-Type: application/json

{
    "refresh": "<refresh_token>"
}
```
Here, Response is access token
![alt text](media/31_JWT_refresh_request.PNG)

SO when access token expires, it return 401 Unauthorized reponse of invalid token on REACT or Vue or React Native application.
Thus exchange refresh token for new access token.

Similarly for verify endpoint, send following POST request and reponse will be 200 OK or 401 Unauthorized
```
POST http://localhost:8000/auth/jwt/verify/ HTTP/1.1
Content-Type: application/json

{
    "token": "access_or_refresh_token_id"
}
```
![alt text](media/31_JWT_verify_request.PNG)
