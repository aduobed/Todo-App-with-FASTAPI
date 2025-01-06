A todo app using FASTAPI

## Fix for Passlib Bcrypt error warning

'''
version = \_bcrypt.**about**.**version**
'''

In the _.venv\Lib\site-packages\passlib\handlers\bcrypt.py_ file change the below line

version = \_bcrypt.**about**.**version**
-->
version = \_bcrypt.**version**
