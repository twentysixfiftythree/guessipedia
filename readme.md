If necessary
python3 manage.py makemigration
python3 manage.py migrate

Add urls in "add_to_db.py" to db:
python3 manage.py runscript add_to_db
python3 manage.py runserver

view db:
navigate to "url/admin" in browser
sign in with u:admin p:admin
