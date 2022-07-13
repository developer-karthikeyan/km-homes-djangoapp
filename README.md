### Project:
* **KM-Homes** - Aim of this application is to serve Seller, Buyer, Realtor in most efficient way.
---
### Project Description:
* **KM-Homes** - Aim of this application is to serve Seller, Buyer, Realtor in most efficient way.
---
<!-- ###Motivation:
* One of my friend asked me to create Realestate application for his Business.
--- -->
### Structure & Design Principle:
<img src='read_me_images/design_principle.jpg'/>

---
### Frameworks & Applications used:
* Django, Bootstrap, HTML, CSS, JS, Heroku, Postgresql
---
### Featured Pages:
* **Register** - Helps User to Create his/her account.
* **Login** - Helps User to login his/her account.
* **Home** - Consists of Search & Latest Property details.
* **Properties** - Shows List of properties for sale.
* **About Us** - Shows Company policies & Team details.
* **Contact Us** - It helps Sellers to communicate with KM-Homes Teams.
* **Dashboard** - Shows Inquired Porperty details of User.
* **Profile** - Helps User to maintain his/her profile details.
* **Logout** - Helps User to logout from his/her account.
---
### Register - page:
* Helps User to Create his/her account.

<img src='read_me_images/registration/reg1.png'/>
<br>

* Each & Every fields have its own validaition functionality.

<img src='read_me_images/registration/reg_v.png'/>

* Successful Registration navigates User to Login page.

<img src='read_me_images/registration/reg2.png'/>

<img src='read_me_images/registration/reg3.png'/>

---
### Login - page:
* Helps User to login his/her account.

<img src='read_me_images/login/login1.png'/>
<br>

* Both fields have its own validaition check.

<img src='read_me_images/login/login_v.png'/>

* Successful Login navigates User to Dashboard page.

<img src='read_me_images/login/login2.png'/>

<img src='read_me_images/login/login3.png'/>

---
### Home - page:
* Consists of Search & Latest Property details.

<img src='read_me_images/home/1.png'/>

* Search form helps to render Properties based on search parameters.

<img src='read_me_images/home/2.png'/>

<img src='read_me_images/home/3.png'/>

* If none of the search criteria is mentioned, then Search form will render all Properties listed in our website.

<img src='read_me_images/home/4.png'/>

<img src='read_me_images/home/5.png'/>

---
### Properties - page:
* Shows List of properties for sale.

<img src='read_me_images/properties/1.png'/>

* User can view interested property details by clicking "More info".

<img src='read_me_images/properties/2.png'/>

* If User is interested in property, then he/she can raise Inquiry by clicking "Make an Inquiry".

<img src='read_me_images/properties/3.png'/>

* If User made successful inquiry then he/she will recieve Confirmation mail from KM-Home team.

<img src='read_me_images/properties/5.png'/>
<img src='read_me_images/properties/6.png'/>

* Similarly, property's realtor will get notification mail from KM-Home team.

<img src='read_me_images/properties/7.png'/>
<img src='read_me_images/properties/8.png'/>

* If User made successful inquiry then he/she will get Success message notification.

<img src='read_me_images/properties/success.png'/>

* Similarly, successfully inquired property will get added to Dashboard page.

<img src='read_me_images/properties/9.png'/>

* Else, If User tries to raise multiple inquiry for same property then he/she will get Error message notification.

<img src='read_me_images/properties/fail.png'/>

---
### About Us - page:
* Shows Company policies & Team details.

<img src='read_me_images/basic_pages/about.png'/>

---
### Contact Us - page:
* It helps Sellers to communicate with KM-Homes Teams.

<img src='read_me_images/contact_us/1.png'/>
<img src='read_me_images/contact_us/2.png'/>

* Requester will get notification mail from KM-Homes Teams. 
<img src='read_me_images/contact_us/3.jpg'/>
<img src='read_me_images/contact_us/4.png'/>

* If request is raised successfully, he/she will get redirected to home page.
<img src='read_me_images/contact_us/5.png'/>

* Else, If requester mentioned any invalid parameters, then he/she will get validation message.
<img src='read_me_images/contact_us/fail.png'/>

---

### Dashboard - page:
* It help to keeps track of inquires which are made by users.

<img src='read_me_images/dashboard/1.png'/>

<img src='read_me_images/dashboard/2.png'/>

---
### Profile - page:
* Helps User to maintain his/her profile details. 

<img src='read_me_images/profile/1.png'/>

* If User tries to update valid profile information, then he/she will get success notification. 

<img src='read_me_images/profile/2.png'/>

* Else, User will get validation error message for respective fields.

<img src='read_me_images/profile/3.png'/>

---
### Logout - page:
* Helps User to logout from his/her account & get navigated to Home page with success message.

<img src='read_me_images/logout/1.png'/>
<img src='read_me_images/logout/2.png'/>

---

## Extra Features:

* Passwrod reset
* Change password
* Authorised user only have access to Dashboard/Property/Profile page

---

### Password reset:
* Helps User to reset his/her password. click "Forgot password?" from login page.

<img src='read_me_images/reset_pwd/1.png'/>

* User should enter his/her registered email address.

<img src='read_me_images/reset_pwd/2.png'/>

* It will send "Reset Password" link to registered email address.

<img src='read_me_images/reset_pwd/3.png'/>
<img src='read_me_images/reset_pwd/4.png'/>
<img src='read_me_images/reset_pwd/5.png'/>

* It will redirect User to "Password Reset" page.

<img src='read_me_images/reset_pwd/6.png'/>

* Finally, User get success notification for password reset.

<img src='read_me_images/reset_pwd/7.png'/>

---

### Change password:

* Helps User to change his/her password. click "Change Password" from Profile page.

<img src='read_me_images/change_pwd/1.png'/>

* User should enter Old & New password.

<img src='read_me_images/change_pwd/2.png'/>

* Finally, It redirect User to Profile page with success message.

<img src='read_me_images/change_pwd/3.png'/>

---

### Authorised user only have access to Dashboard/Property/Profile page

* After loggout, If user trying to access Dashboard/Property/Profile page. User will get redirected to "Login Page". After successful login User will be redirected to expected page.

* Similarly, above scenario will be applicable for Unauthorized user.

    * https://km-homes-djangoapp.herokuapp.com/accounts/dashboard/
    * https://km-homes-djangoapp.herokuapp.com/listings/7
    * https://km-homes-djangoapp.herokuapp.com/accounts/profile/

* Below I have mentioned only Profile access scenario.

<img src='read_me_images/unauth_protection/1.png'/>

<img src='read_me_images/unauth_protection/2.png'/>

<img src='read_me_images/unauth_protection/3.png'/>

---
### Conclusion:

* If you have read this far I really appreciate it.

* Connect With me at [LinkedIn](https://www.linkedin.com/in/karthikeyan-m-576336240/) & [Github](https://github.com/developer-karthikeyan)

* Do share your valuable opinion, I appreciate your honest feedback!

---
