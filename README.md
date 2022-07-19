### Project:
* **KM-Homes** - Aim of this application is to connect serve Sellers, Buyers, Realtors in most efficient way.
---
### Project Description:
* Aim of this application is to connect serve Sellers, Buyers, Realtors in most efficient way.
---
### Structure & Design Principle:    
<img src='read_me_images/design_principle.jpg'/>

---
### Frameworks & Applications used:
* Django, Bootstrap, HTML, CSS, JS, Heroku, Postgresql
---
### Featured Pages:
* **Register** 
* **Login**
* **Home** 
* **Properties** 
* **About Us** 
* **Contact Us**
* **Dashboard**
* **Profile** 
* **Logout** 
---
### Register page:
* Helps User to Create his/her account.
    <img src='read_me_images/registration/reg1.png'/>
    <br>
  
* If User gave valid parameters then he/she will get Registered & navigated to Login page.
    <img src='read_me_images/registration/reg2.png'/>

    <img src='read_me_images/registration/reg3.png'/>
    <br>

* Else, User will get **validation errors** based on the given parameters.
    <img src='read_me_images/registration/reg_v.png'/>
    <br>
---
### Login page:
* Helps User to login his/her account.
    <img src='read_me_images/login/login1.png'/>
    <br>

* If User gave valid credentials, then he/she will get Loggedin & get navigated to Dashboard page.
    <img src='read_me_images/login/login2.png'/>

    <img src='read_me_images/login/login3.png'/>
    <br>

* Else, User will get **validation errors** based on the given parameters.
    <img src='read_me_images/login/login_v.png'/>
---
### Home page:
* It Consists of Search feature & Latest Property details.
    <img src='read_me_images/home/1.png'/>
    <br>

* Search feature helps User to find expected Properties from all states in India.
    <img src='read_me_images/home/2.png'/>

    <img src='read_me_images/home/3.png'/>
    <br>

* If none of the search criteria is mentioned by User, then Search feature will shows all the Properties listed in website.
    <img src='read_me_images/home/4.png'/>

    <img src='read_me_images/home/5.png'/>
---
### Properties page:
* It shows complete list of properties for sale.
    <img src='read_me_images/properties/1.png'/>
    <br>

* User can view specific property details by clicking **"More info"**.
    <img src='read_me_images/properties/2.png'/>
    <br>

* If User is interested in this property, then he/she can raise Inquiry by clicking **"Make an Inquiry"**.
    <img src='read_me_images/properties/3.png'/>
    <br>

* If User made successful inquiry, then he/she will recieve Confirmation mail from **KM-Home team**.
    <img src='read_me_images/properties/5.png'/>
    <br>    
    <img src='read_me_images/properties/6.png'/>
    <br>

* Similarly, respective realtor for that property will also get notification mail from **KM-Home team**.
    <img src='read_me_images/properties/7.png'/>
    <br>    
    <img src='read_me_images/properties/8.png'/>
    <br>

* If User made successful inquiry, then he/she will get **Success notification**.
    <img src='read_me_images/properties/success.png'/>
    <br>

* Also inquired property will get added to User's Dashboard page.
    <img src='read_me_images/properties/9.png'/>
    <br>

* Users are allowed to raise only one inquiry for a property.
* If User tries to raise multiple inquiries, then he/she will get **Error notification**.
    <img src='read_me_images/properties/fail.png'/>
---
### About Us page:
* It shows Company policies & Realtor team details.
    <img src='read_me_images/basic_pages/about.png'/>
---
### Contact Us page:
* Sellers can post their queries to KM-Homes teams through this contact form.
    <img src='read_me_images/contact_us/1.png'/>
    <img src='read_me_images/contact_us/2.png'/>
    <br>

* For every successfully post, Requester will get notification mail from KM-Homes Teams. 
    <img src='read_me_images/contact_us/3.jpg'/>
    <br>    
    <img src='read_me_images/contact_us/4.png'/>
    <br>

* If request is raised successfully, he/she will get redirected to home page.
    <img src='read_me_images/contact_us/5.png'/>
    <br>

* Else, Requester will get **validation errors** based on the given parameters.
    <img src='read_me_images/contact_us/fail.png'/>
---
### Dashboard page:
* It helps to keep track of User's inquiry list.
* Newly registered User won't have inquiry list.
    <img src='read_me_images/dashboard/1.png'/>
    <br>    
* Existing User's inquiries are listed in Dashboard.    
    <img src='read_me_images/dashboard/2.png'/>
---
### Profile page:
* It helps User to maintain his/her profile details. 
    <img src='read_me_images/profile/1.png'/>
    <br>

* If User provided valid parameters. Those details got updated & he/she will get **Success notification**. 
    <img src='read_me_images/profile/2.png'/>
    <br>

* Else, User will get **validation errors** based on the given parameters.
    <img src='read_me_images/profile/3.png'/>
---
### Logout page:
* It helps User to logout from his/her account & get navigated to **Home page** with **Success message**.
    <img src='read_me_images/logout/1.png'/>
    <img src='read_me_images/logout/2.png'/>
---
## Extra Features:

* Password reset.
* Change password.
* Preventing Dashboard/Property/Profile pages from Unauthorized User.
* Administrator's Admin Panel.
---
### Password reset:
* click **"Forgot password?"** from login page.
    <img src='read_me_images/reset_pwd/1.png'/>
    <br>

* User should enter his/her registered email address.
    <img src='read_me_images/reset_pwd/2.png'/>
    <br>

* It will send **"Reset Password"** link to registered email address.
    <img src='read_me_images/reset_pwd/3.png'/>
    <img src='read_me_images/reset_pwd/4.png'/>
    <br>
    <img src='read_me_images/reset_pwd/5.png'/>
    <br>

* After clicking the link, It will redirect User to **"Password Reset"** page.
    <img src='read_me_images/reset_pwd/6.png'/>
    <br>

* Once password reset was done. Finally, User get **success notification**. Now, User can able to login with his/her new passsword.
    <img src='read_me_images/reset_pwd/7.png'/>
---
### Change password:

* click **"Change Password"** from Profile page.
    <img src='read_me_images/change_pwd/1.png'/>
    <br>

* User should enter valid **"Old"** & **"New"** password.
    <img src='read_me_images/change_pwd/2.png'/>
    <br>

* Once password got changed. Finally, User will get redirected to **"Profile page"** with **success notification**.
    <img src='read_me_images/change_pwd/3.png'/>
---
### Preventing Dashboard/Property/Profile pages from Unauthorized User:

* After logout, If user trying to access his/her **Dashboard/Property/Profile** page. User will get automatically redirected to **"Login Page"**. After successful login User will get redirected to expected page.
    <br>

* **Dashboard/Property/Profile** page links for reference:
    * https://km-homes-djangoapp.herokuapp.com/accounts/dashboard/
    * https://km-homes-djangoapp.herokuapp.com/listings/7
    * https://km-homes-djangoapp.herokuapp.com/accounts/profile/
    <br>

* Here, I have mentioned only **Profile page** access scenario. For example, after successful logout User trying to access his/her Profile page.
    <img src='read_me_images/unauth_protection/1.png'/>
    <br>
* User will get automatically redirected to **"Login Page"**.
    <img src='read_me_images/unauth_protection/2.png'/>
    <br>
* After successful login, User will be taken to expected **Profile page**.
    <img src='read_me_images/unauth_protection/3.png'/>
---

### Admin Panel for administration purpose:

* KM Homes website admin page.
    <img src='read_me_images/admin_panel/admin.png'/>
    <br>
* Administrator has full access to **add/remove Properties** from **Listings** tab.
    <img src='read_me_images/admin_panel/listing.png'/>    
    <img src='read_me_images/admin_panel/listing2.png'/>
    <br>
* Similarly, Administrator has full access to **add/remove Realtor** from **Realtors** tab.
    <img src='read_me_images/admin_panel/realtor.png'/>    
    <img src='read_me_images/admin_panel/realtor2.png'/>
---

### Future Updates:

* Gmail or Facebook account based **User Signed Up**.
* **Google maps** feature to show exact location of Property.
* **Machine Learning** feature for Property search.
* **Data Analytics** feature to generate reports for Property sale.
---

### Conclusion:

* Thanks for reading this Document. I really appreciate your Patience & Effort.

* Kindly please share your valuable feedback & comments through ( +91-9585675562, productdeveloper.karthikeyan@gmail.com ).

* Connect with me at [LinkedIn](https://www.linkedin.com/in/karthikeyan-m-576336240/) & [Github](https://github.com/developer-karthikeyan).
---