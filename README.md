# student-project
Download and install python3 and verify if the path is set.
Download and install pip for python3.
pip install virtualenv
Create vitrual environment:  
        a)Linux/MacOS: virtualenv env -p python3
        b)Windows: virtualenv env
Activate vitrual environment: 
        a)Linux/MacOS: . env/bin/activate
        b)Windows: env\Scripts\activate
Go to project folder:  cd project_folder/
Install packages: pip install -r requirements.txt
Create migrations:
       A. ./manage.py makemigrations student
       B. ./manage.py migrate student

Create Superuser: ./manage.py createsuperuser
Run server:  ./manage.py runserver
