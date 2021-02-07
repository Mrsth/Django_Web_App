# Django_Web_App

<h2>A web application practice 2021/Jan/25</h2>
<hr>
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

<h2>A web application practice 2021/Jan/26</h2>
<hr>
<p>
  <h3> User validation and message</h3>
  <img src="Images for github/user_validation_and_message.PNG"/>
  In views.py file import UserCreationForm and message. Then check the method of the form, if the method is "POST" then run the code. After that create the
  instance of the UserCreationForm having the value entered from the form. Then validate if the provided input is correct/valid or not. Now, save the user which 
  will be recorded in the database.
  
  In base.html alert-{{message.tags}} will give the respective type of alert. If it is success alert the success alert is show, if waring then warning alert is shown.
</p>

<p>
  <h3>Customizing the form</h3>
  <img src="Images for github/Custome_registration_form.PNG"/>
  The above image shows how we can customize the form made in django. In views.py replace UserCreationForm by custom form "RegistrationForm". 
  <ul>
    <li>First create a form.py in the respective app</li>
    <li>Do the necessary importing as above.</li>
    <li>Now create the Signupform which inherits the UserCreationForm</li>
    <li>Create the required field example email. model=User means perform modification in User model. Field means show the fields in the same order.</li>
  </ul>
</p>

<p>
  <img src="Images for github/Crispy.PNG"/>
  In order to make form look good, we have used Django Crispy.
  <ul>
    <li>Refer this for installing the crispy django form: https://django-crispy-forms.readthedocs.io/en/latest/install.html</li>
    <li>Now load the crispy form tag in the required html and do this {{signup | crispy}}</li>
  </ul>
</p>


<h2>A web application practice 2021/Jan/28</h2>
<hr>
<div>
  <h3>How to make login form?</h3>
  <p>
    First of all import the LoginView and LogoutView as show below:
    <img src="Images for github/Login_logout_view.PNG"/>
    LoginView and LogoutView are classed based view.
  </p>
  <p>
    Now make the html page for login and logout as follows:
    <img src="Images for github/Login_logout_html.PNG"/>
  </p>
  <p>
    Now make dynamic navbar. I.e. only show login and register if the user is not logged in else show only logout button.
    <img src="Images for github/Dynamic_login_logout_button.PNG"/>
  </p>
  <p>
    Now if the user logged in then the django will redirect the user into its own default page like "/accounts/profiles".But we
    need to redirect the user into custom made page. For this we have to make some changes in the setting.py file of the project 
    like below:
    <img src="Images for github/Login_redirect_url.PNG"/>
  </p>
<div>
  
<div>
   <h3>How to restrict url?</h3>
   <p>
      Import the following decorator:
   </p>
   <img src="Images for github/Login required.PNG"/>
   <p>
      As a result of the dash.html will only be accessible after login. Now if the login is incorrect then the user will be redirected to
      the django default page. To redirect to the required page then do some modification in the setting file as follows:
   </p>
   <img src="Images for github/Login url.PNG"/>
</div> 

<div>
  <h2>A web application practice 2021/Feb/2</h2>
  <hr>
  <h3>How to update Form Using ModelForm?</h3>
  <b>STEP 1:</b><p>First of all import necessary importings for this modelform we need "from django import forms"</p>
  <img src="Images for github/ModelForm_1st_step.PNG"/>
  <p>
    From above diagram we can see that "UserUpdateForm" and "ProfileUpdateForm" are the two modelform used to update the model
    "User" and "Profile" respectively. Django ModelForm is a class that is used to directly convert a model into a Django form.
    For more about django modelform click the link below: https://www.geeksforgeeks.org/django-modelform-create-form-from-models/
    In UserUpdateForm we can see that there is email field. It is the way we add our own required field in the defaulr django form.
    In UserUpdateForm email, and username are the attribute of the class User model just like image is the attribute for the Profile model.
  </p>
  <b>STEP 2:</b><p>Creating the instances of the modelform</p>
  <img src="Images for github/ModelForm_2nd_step.PNG"/>
  <p>
    Now we have to create the instances of the modelform in the required views.py file. Here we need to create the update form in the dashboard
    we create the instances in the dash function and pass the instances in the context.
  </p>
  
  <b>STEP 3:</b>
  <p>Showing the instances and encoding/p>
  <img src="Images for github/ModelForm_3rd_step.PNG">
  <p>
    Now we show the passed instances from the context into the html page. Also we need to type enctype="multipart/form-data" in the form tag.
    This will help in the proper loading of the images for the profile picture.
  </p>
  
  <div>
   <h2>A web application practice 2021/Feb/3</h2>
   <hr>
   <h3>Solving the error of not showing the default image</h3>
   <img src="Images for github/default_profile_pic.PNG"/>
   <p>
     The problem occured because, when django tried to render the default image for the user having no profile picture then we have just
     defined that thing in the program. I.e we have not created object for each profile of each user. So when django try to render the
     image then there will be no object of the user so it will not render anything. At first we create the object manually but later on
     we will use signal for not doing it automatically. If we don't use signal then we must go to admin and create the object of each user
     created and add image to that object.
  </p>
  </div>
  
  <div>
    <h2>A web application practice 2021/Feb/5</h2>
    <hr>
    <h3>Signal practice</h3>
    <img src="Images for github/Signal_instruction_step1.PNG"/>
    At first create a signals.py file in the app where we need to use the signals then import the User as well as signals as shown in the figure above.
    user_logged_in, user_logged_out, user_login_failed are the signals. And User is the signal sender. Now its time to make a signal receiver. E.g: 
    login_signal_handler, and logout_signal_handler as shown in the figure above. Now we need to connect the receiver the signal with the respective
    receiver otherwise signals won't know which way to go and signal receiver won't know which signal to receive. So for this we have two ways:
      - <b>Manual Connect Route:</b> In this way we use signal.connect(signal_handler, sender=User). In above figure this way is commented out at the
        bottom.
      - <b>Decorator:</b> To use this way we need to import "from django.dispatcher import receiver". And after that add the decorator at the top of the
        respective signal receiver function as shown in the figure above.
    
   Now we need to do two more configurations as follows:
   <img src="Images for github/Signal_instruction_step2.PNG"/> 
   <img src="Images for github/Signal_instruction_step3.PNG"/>
   While installing the app after using the signal, it is very mandatory to write the code as it is in the above image.
  </div>
</div>
