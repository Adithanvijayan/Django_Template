
// Create Virtual Environment 
pip install virtualenv
virtualenv --version
virtualenv env_name
source env_name/bin/activate

// Install Django and Create a project
python -m pip install Django
python -m django --version
django-admin startproject Project_Name

// Navigate to Project Folder
cd Project_Name/

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

// create a application for project
python manage.py startapp app_name
python manage.py runserver

//add lines in settings.py
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) // for image files
ALLOWED_HOSTS = ['*']
'app_name' in INSTALLED_APPS
'DIRS': [TEMPLATE_DIR,] in TEMPLATES

//add lines in urls.py
from django.urls import path,include
path('',include('app_name.urls')),

//create templates folder in Project_Name Main Folder - for HTML files
//create html files in templates folder
//create static folder in Project_Name Main Folder - for image files
//create image folder in static folder
//create image files in image folder inside the static folder
//create urls.py in app_name folder

//add lines in urls.py inside the app_name folder
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index")
]

//add functions in views.py file - named as in urls.py file inside the app_name folder
def index(request):
    return render(request,'index.html')

//create tables for database in models.py inside the app_name folder
import uuid
class table_name(models.Model):
    unique_id = models.UUIDField(primary_key=True, null=False , default=uuid.uuid4, editable=False)
    integer_field = models.IntegerField()
    char_field = models.CharField(max_length = 50, null=False)
    textarea_field = models.TextField()
    def __str__(self):
        return '{}'.format(self.integer_field)  

//Register the tables in admin.py inside the app_name folder
from .models import table_name
admin.site.register(table_name)
