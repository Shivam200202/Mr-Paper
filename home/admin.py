from django.contrib import admin
from home.models import Contact

# Register your models here.
admin.site.register(Contact)

# You will able to see at admin panel
# Now register app by home.apps > copy HomeConfig > hello.settings(project.settings) and find "INSTALLED_APP" and paste "home.apps.HomeConfig"
#then "python manage.py makemigrations" and python manage.py migrate