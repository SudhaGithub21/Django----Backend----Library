# Django Bootcamp - Ailaysa Technologies Private Limited

In the bootcamp session, I learned a lot about Ailaysa, a collaborative platform for project management, managing linguistic assets, team coordination, assignment tracking, and integration. I found your company's workflows very interesting. Your focus on a generative AI platform for creating multilingual and multi-modal content is impressive. You cover many aspects of content,including translation, creation, transformation, and discovery.

You taught the basics of the Django framework and guided us through a simple project called "movie_portal". This helped us understand how to start a project and run it using Django commands.

Now, I am working on a backend project called Library Management System using the Django framework. I share my daily activities and project progress on GitHub to keep track of how the project is going.

1. To create the project, run:
   # django-admin startproject library
2. To create an app for it, run:
   # python manage.py startapp library_manage
3. To create a database, add models in the models.py file in the library_manage app.After creating the models, migrate the database with:
   # python manage.py makemigrations
   # python manage.py migrate
4. Add the app in the INSTALLED_APPS section of settings.py in the library project folder.Create a superuser to access the database in the admin interface by running:
   # python manage.py createsuperuser
5. Study and practice basic ORM using the interactive shell:
   # python manage.py shell
6. Create a serializers.py file in the library_manage app folder.Perform serialization and deserialization using ORM in the interactive shell:
   Serializable: Outward Data - Data from the database is represented to the requesting server.
   Deserializable: Inward Data - To input data into the database.
7. Create a urls.py file in the library_manage app folder and add the app URLs to the project's urls.py file.
8. Finally, run the server:
   # python manage.py runserver
9. Pass the URLs to create, read, update, and delete the data.
   This workflow has been very helpful for me in building and managing the project.


