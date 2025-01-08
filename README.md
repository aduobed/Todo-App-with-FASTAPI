A todo app using FASTAPI

## Fix for Passlib Bcrypt error warning

'''
version = \_bcrypt.**about**.**version**
'''

In the _.venv\Lib\site-packages\passlib\handlers\bcrypt.py_ file change the below line

version = \_bcrypt.**about**.**version**
-->
version = \_bcrypt.**version**

## Generate requirements.txt from pipenv
> pipenv requirements > requirements.txt

## Data Migration With Alembic
Alembic is a powerful tool that allows us to modify database schemas.
1. Alembic provides the creation and invocation of change management scripts.
1. This allows you to create migration environments and also change data how you like.
1. It allows you to modify your database in real-time 