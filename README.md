1. Download and install python3 and verify if the path is set.
2. Download and install pip for python3.
3. pip install virtualenv
4. Create vitrual environment:  
   a)Linux/MacOS: virtualenv env -p python3
   b)Windows: virtualenv env
5. Activate vitrual environment:
   a)Linux/MacOS: . env/bin/activate
   b)Windows: mypthon\Scripts\activate
6. Go to project folder: cd project_folder/
7. Install packages: pip install -r requirements.txt
8. Create migrations:
   A. ./manage.py makemigrations student
   B. ./manage.py migrate student

9. Create Superuser: ./manage.py createsuperuser
10. Run server: ./manage.py runserver
