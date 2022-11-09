
##  Test Account:

Email: test@test.com

Username: testuser

Password: test1234

  

#  CS50w Capstone

For the CS50 Web's final project, I've built a password manager app, which allows users, to create an account, log into the account, create different folders, and add different accounts to the folder. Whilst utilizing Django for the backend, JavaScript for the frontend and tailwind for the styling.

  

##  Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.

###  Distinctiveness and Complexity

This project is completely different from all the other projects from the course, whilst making sure to meet all the complexity requirements given in the project.  

The project utilizes Django on the backend, and pure HTML, and JavaScript, with Tailwind CSS on the front-end. I believe the project satisfies the [distinctiveness and complexity requirements]((https://cs50.harvard.edu/web/2020/projects/final/capstone/#requirements)  ) given because, the web app utilizes Django on the frontend, it uses more than one model (3 in total), uses JavaScript in the backend and is completely mobile-responsive.

The project contains 2 apps, one for authentication which contains everything that has to do with the user authentication, and the other app called vault for the actual app, and its functioning.

#### Authentication App:
In the authentication app, I've tried to utilize JavaScript more, since I have been working using more Django code recently and less JavaScript, and so users wouldn't have to re-render the whole page, just because they accidentally clicked on login instead of register or vise-versal. Although, the `get password hint` does take you to a new page, I felt like it would be an overkill trying to add it with the login, and register HTML code. 
When registering, users are prompt to enter an email, username, password, and password hint. I decided on adding the password hint, since a-lot of people might have access to their friends emails, siblings emails or phones, so trying to reset password via an email wouldn't be that secured, hence why I decided on going with the password hint feature, and it was also something I noticed in a password manager I used myself. 
In the password hint field, users are meant to enter something that would remind them their passwords incase they did forget. The password hint is then encrypted using [Fernet (symmetric encryption)](https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption") and stored in the database. I decided on encrypting the password hints, and added a backend check to make sure users do not enter their passwords in their password hint field. As some users could be way too lazy and just decide to have it that way. Another reason behind my decision on encrypting the password hints is, because users can be really explicit with their password hints, even though in my opinion, that would be the users fault, but at the same time, It is my job to try my very best to help secure everything.

#### Vault App
The vault app consists of 3 different pages. I tried keeping the amount of pages small, trying to make use of more JavaScript, and being able to have a good amount of features on one page. 
Users can create folders, edit folders, create items, and edit as well them. Folders are displayed in the aside sidebar, and are displayed in the other of their priority, which the user can set whilst creating or editing a folder. In the aside sidebar, I've also provided a way other than the search functionality for users to filter their items. They can either filter them by their priority or "starred". A user can star an item, incase they need it frequently or an easier way to get to it, so the starred page, would usually consists of the items the user uses most frequently. Passwords, and emails added to the items are all encrypted using the [Fernet (symmetric encryption)](https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption"). So if there was a database leak, or anything related, user's passwords and emails would still be safe.

The index page consists of a consist of a search bar, which could help the user find any of their items, either by the item name, username, URL, user or even if the item notes contains the searched keywords so in that way, it would be hard for people to not find the items they're looking for incase they have a-lot of items.
 
I've also added some JavaScript files, which are mainly there to make the site look, or feel better. Like the `aside.js` which helps in making the navbar mobile-responsive, or the `password.js` which helps with functioning the password generator on the item edit page, the ability to show and hide password as well as the ability to copy the items password. And I've also added the `overlays.js` which basically handles everything that might need to be displayed as a pop out menu. One main way I've seriously utilized it, is whenever the user tries to delete anything, be it a folder or an item, an overlay pops up, asking if they're sure they want to delete the item or folder depending on what they might have clicked on. Another way I've utilized the `overlays.js` file is to display the add folder, or  add item form. 


##  What’s contained in each file you created?

###  Authentication App:

*  `"authentication\urls.py"` Contains the URLs routes for the authentication app.

*  `"authentication\encryption.py"` Contains 2 functions ('encrypt', 'decrypt'), that helps encrypt or decrypt the passed in string and returns the encrypted text.

*  `"authentication\views.py"` Contains the login, logout, register and gethint views.

  

###  Vault App:

*  `"vault\views.py"` Contains the apps views.

*  `"vault\urls.py"` Contains the URLs routes for the authentication app.

*  `"vault\forms.py"` Helps in fully utilizing Django's built-in forms system for pre-filling the form with model data.

  

#####  Other files added:

*  `"authentication\templates\aside.html"` Contains the app's aside menu

*  `"authentication\templates\mainHeader.html"` Contains site's main header

*  `"authentication\templates\nav.html"` Holds the site's navbar.

*  `"authentication\templates\overlays.html"` Contains all the popup menu's. (delete confirmation, create item and create folder)

*  `"authentication\templates\auth\auth.html"` Contains everything needed for user authentication in the frontend.

*  `"authentication\templates\auth\gethint.html"` Helps in retriving users password hint.

*  `"authentication\templates\vault\index.html"` The main site page.

*  `"authentication\templates\vault\item.html"` Holds everything needed for editing an item

*  `"authentication\templates\vault\editFolder.html"` Holds everything needed for editing a folder.

*  `"authentication\static\password.js"` Handles the password generator, and copying the password.

*  `"authentication\static\overlays.js"` Handles the overlays functionality for displaying the right overlay at the right time.

*  `"authentication\static\auth.js"` Helps in switching from login form to register and vise versa

*  `"authentication\static\aside.js"` Used in making the aside menu mobile friendly.

  

*  `"theme\templates\base.html"` The main html layout, generated by tailwind css.
*   

##  How to run the application:

* CD into the project directory

* Create a virtual environment, and activate it

* Run pip install -r requirements.txt in your shell.

* Run "python manage.py runserver" to run the project.

* The app should be running on [127.0.0.1:8000](127.0.0.1:8000)

  
  

:arrow_forward: &nbsp;  **View Live Demo [here](https://youtu.be/N07PgXOyiP4)**
