# Django_Web_App

<h2>A web application practice 2021/Jan/25</h2>
<img src="Images for github/Dashborad.PNG">
<p>This is the dashboard of the web application under construction. Here, there is a navbar and we can see some posts as well. 
For now let this be just a dummy variables in the context which is passed on to the html page. 
Further on we will create a database which will store the post content like post author, post content, post date.
</p>

<p>
Instead of creating the model and perofrming authentication of that user manually, we can use the User defined by the django itself.
"from django.contrib.auth.models import Users"

Next we will create a Post model. One user can post multiple post i.e one to many relation. But one post cannot have many user.
So, the primary key of the user model can be used as foreign key for the Post model.

In this way we created two models namely User and Post. Now run following command:
- python manage.py makemigrations
- python manage.py migrate
If you want to see the models in the admin panel then you need to register both of the models in the admin.py of the respective app.
</p>

<h2>Work in python shell </h2>
<p>
  Now that we have created the required models, its timme to fetch the data from the database and passing it to the respective html to show the
  fetched value. Therefore we use python shell to check the fetching process. To run the shell type python manage.py shell.
  <img src="Images for github/PyhonShell.PNG"/>
</p>

<p>
  Put the fetched data into the context and pass it to the respective html page.
</p>
