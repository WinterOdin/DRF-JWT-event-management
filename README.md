## Django JWT Event management
This is simple API for event managment, to make API calls use postman or via DRF interface just remove code bellow from settings 
```
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
```
There is schema and documentation available under
```
/schema/
/docs/
```
To register as a new user
```
/api/user/register/
```
to obtain JWT token 
```
/api/token/
```
### How to run it
Just create env and install dependencies
```
pip install -r req.txt
```
and then
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```