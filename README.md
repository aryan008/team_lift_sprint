<h1 align = "center">Team Lift Sprint</h1>

View the live project at the following [link](https://adam-team-lift-sprint.herokuapp.com/).

![See how the site looks across the devices](media/readme/responsive-view.JPG)

Team Lift Sprint is an online shopping site that sell a manner of goods related to sport and/or sporting equipment. It is designed for Strength & Conditioning coaches, team managers, players and those focusing on getting the best out of their performance. The website provides status and feedback to users at all stages of the shopping process, as well as items on sale and correct UX design. Coming from a sporting background myself, the site itself comprises a number of categories which are discussed in detail below with the aim that Team Lift Sprint be a "one stop shop" for all those either training individually or in a group.

Categories are split between individual & team, with durther drilldowns into these whether they are indoor/outdoor, track, cardio, gym or cardio. The site is to encompass a one stop shop for all visitors, including a TLS blog where useful articles can be added. Logged in users will have the abilty to create a review of a product to help guide prospective purchasers for items, giving them an incentive to create an account and have their own profile page.

The site has been tested on a number of devices including desktop, tablets and mobile - as shown in the testing readme file. The site is also designed to handle the full suite of user management, as defined in the Information architecture of this ReadMe file.

## Table of Contents
* [Site Owner/Developer and Product/Business Goals](#site-owner/developer-and-productbusiness-goals)
* [First Time Visitor Goals](#first-time-visitor-goals)
* [Returning and Frequent Visitor Goals](#returning-and-frequent-visitor-goals)
* [User Experience (UX)](#user-experience-ux)
  * *The 5 planes of User Experience – Decisions and Reasons*
   1.	[Strategy plane](#strategy-plane)
   2.	[Scope plane](#scope-plane)
   3.	[Structure plane](#structure-plane)
   4.	[Skeleton plane](#skeleton-plane)

* [Design Features](#design-features)
  1. [Wireframes](#wireframes)
  2.	[Typography](#typography)

* [Design & UX – How do they come together?](#design--ux--how-do-they-come-together)
  * [User goals](#user-goals)
  * [Site owner/designer goals](#site-owner/designer-goals)
  * [Application-features](#application-features)
  * [Future-developments](#future-developments)

* [Information Architecture](#information-architecture)
  *	[Site Logic and diagram](#site-logic-and-diagram)
  *	[User Types and permissions](#user-types-and-permissions)
  *	[CRUD Functionality](#crud---create-read-update-and-delete)
  *	[Database model](#database-model)

* [Technology and Languages used](#technology-and-languages-used)
  *	[Languages](#languages)
  *	[Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)

* [Testing](#testing)

The following areas of testing were reviewed:
  * Code validation
  * Accessibility testing
  * Responsive testing
  * Manual testing
  * Testing user stories from User Experience (UX) section
  * Known bugs

* [Deployment](#deployment)
  * [Process of deployment](#process-of-deployment)
  * [How to run this project locally](#how-to-run-this-project-locally)

* [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)


## Site Owner/Developer and Product/Business Goals
As the developer, the site is to achieve the following goals:
1.	Achieve the user goals as specified below
2.	Create a positive experience for all user types using the specifications required
3.	Achieve responsive design across all devices
4.	Utilize the combination of HTML, CSS, JavaScript and Python to enhance the experience of the user
5.	Become a hub for sportspeople to purchase fitness equipment
6.	Allow “superuser” access to designated personnel to manage store products in full - CRUD functionality
7.	Ensure the site is secure

## First-Time Visitor Goals
As a first-time visitor of the site, I want:

1.	My impression of the site to be a positive experience
2.	To understand the main purpose of the site
3.	To purchase relevant equipment related to individual/team sports
4.	Create a profile - including login/register functionality
5.	An instant feedback loop from site navigation on what I am doing
6.	Easy navigation of the site including searching for a term
7.	Built-in safety protocols – user authentication, appropriate redirects, site action feedback
8.	The ability to edit/delete any items in my bag
9.	Secure card payment protocols
10.	Ability to view my checkout items if I have accidentally exited the site
11.	Buy an item without registering
12.	Browse products easily including sorting them
13.	View and purchase whats on sale
14.	Have a FAQ section where I can get in touch with the company regarding shipping/delivery, etc.
15.	See if I have any shipping costs
16.	See any product reviews and enter one myself
17.	Read any articles regarding fitness


## Returning and Frequent Visitor Goals
1.	Ability to reset my password and forgot my password verification
2.	View my previous orders
3.	Log in and out easily
4.	Save/Update my contact details


## User Experience (UX)
### _The 5 planes of User Experience – Decisions and Reasons_
#### Strategy Plane

Question |	Response for site design
-------- | ---------
Is the content culturally appropriate? |	Design will be simplistic in terms of UX and is based on leading sporting equipment sites - dark initial interface with training images and clear product viewing
Is the content relevant? |	Acting as an training product hub, only relevant “Training” content will be displayed
Can we provide content in an intuitive way? |	The site will have a series of toast messages/redirects/buttons and, using Python and JavaScript, will feel interactive to the site user. Django's allauth functionality manages the user from registration to their profile management
Is the technology appropriate? |	Team Lift Sprint is essentially a online training store with CRUD functionality for all user types (Visitor/user/superuser), and as such Django/Python is the primary source of technology for the site back-end. A combination of CSS and JavaScript will be used for applicable user experience on the front-end
Who is my target audience? |	Discussed in the opening part of this ReadMe.
Product considerations |	No overload of content/imagery on the site as per appropriation. Clear feedback loops from must be present for all user types on what they are clicking on in the site. Navigation/layout must be easy across all devices for the users

##### Strategy feasibility scoping
Opportunity |	Importance |	Feasibility
-------- | --------- | -----------
Ability for unregistered users to purchase an item | 5 | 5
CRUD functionality on user's bag items regardless of registered or not | 5 | 5
Django allauth technology for registration and managing of user accounts | 5 | 5
Feedback loops on all site users CRUD Functionality with regards to items - messages of bag edits | 5 | 5
Success message on purchasing an item, including order number and confirmation | 5 | 5
Ability for logged in users to view their profile and saved address | 4 | 5
A section allowing the users to purchase recommended items based on their interests - e.g. a track athlete on grass | 3 | 2
Superuser functionality to to perform CRUD operations on all items | 5 | 5
Pagination on all products view | 3 | 2
User error handling – appropriate redirects on user interaction and display message | 5 | 5
Wish List | 3 | 1
A split of products based on what the user is looking for - themselves/team/indoor/outdoor | 3 | 5
Footer links include FAQ's that is standard across all ecommerce sites | 4 | 5
Varying product images for each product (side view/back) | 3 | 3
Integration of secure payment system | 5 | 5
Calculations for VAT & postage in different countries | 4 | 1
Cart products saved to profile | 4 | 3
Pre paying the user has the ability to edit their bag items | 5 | 5
Sort functionality on all product views | 3 | 5
Title on products page for categories | 3 | 5
Pagination | 3 | 5
Products on sale are clearly defined and shown how much the user saves by purchasing | 4 | 5
Allow logged in users to submit a review of a product and see other reviews | 3 | 5
Site admins can post fitness related content as a blog | 4 | 4

#### Scope Plane
What's in? |	What's out?
-------- | ---------
Ability for unregistered users to purchase an item | A section allowing the users to purchase recommended items based on their interests - e.g. a track athlete on grass
CRUD functionality on user's bag items regardless of registered or not | Varying product images for each product (side view/back)
Django allauth technology for registration and managing of user accounts | Pagination
Feedback loops on all site users CRUD Functionality with regards to items - messages of bag edits| Wish List
Success message on purchasing an item, including order number and confirmation | Calculations for VAT & postage in different countries
Ability for logged in users to view their profile and saved address | Cart products saved to profile
Superuser functionality to to perform CRUD operations on all items | Title on products page for categories
Pagination on all products view
User error handling – appropriate redirects on user interaction and display message
A split of products based on what the user is looking for - themselves/team/indoor/outdoor
Footer links include FAQ's that is standard across all ecommerce sites
Integration of secure payment system
Allow logged in users to submit a review of a product
Pre paying the user has the ability to edit their bag items
Sort functionality on all product views
Site admins can post fitness related content as a blog
Products on sale are clearly defined and shown how much the user saves by purchasing

#### Structure Plane
Question |	Response for site design
-------- | ---------
How do I navigate easily? | Navbar is present across all site pages and is fixed to the top. Pages present on the account management section of the navbar will depend on the following: Unregistered user - On the home page, prompt to create an account/login. Home/product sections are present regardless of user status. Blog section is available to all user types Registered user – As above but including navbar links for profile page as well as log out option. Users can also review products. Superuser – As above but including a navbar link for managing the site products. Throughout the site, buttons/navbar links are present to allow the user to bring them to the areas they wish to visit. On the products pages, a "bring to top" button is available for the user to click rather than scrolling needlessly back up. Superusers can also delete reviews as well as full CRUD usage on blog posts.
How is the information presented? | Using sporting equipment site style colours/features and text content that allow the user to achieve their goals. Dark navbar background to light product interface for a clear separation of site navigation to bag additions/management. Clear feedback loop for all users whenever the user performs CRUD functionality. The buttons through the site pop to the user, clearly demonstrating what will happen should they click on them.
State changes | There is a clear state change at the navbar level depending on the user of the site as previously mentioned – no account, registered user, superuser. Appropriate redirects/CTA buttons are present when the user interacts with both the navbar and the buttons of the site, including “keep shopping”/"checkout securely"/"View bag" both in the html pages and the toast forms. Upon checking out, a clear state change a success message appears for the order which allows them to see their purchase. Finally, state changes are present on all CRUD function buttons when the user interacts with them along with the Toast messages, tying in with the feedback loop that the user action was performed successfully.
Is the site consistent? | Correct styling and fonts are applied throughout the site, which was achieved using the "extends" functionality in Django.
Is the site predictable? | All navigation is familiar to the user in terms of font/styling consistency.
Is the site appropriately visible? | See the testing section of this ReadMe file for visibility testing.
How does the user know to scroll/what to do? | Clear CTA buttons on the site landing page on where the user wishes to visit.
What if a user makes a mistake on their bag and wishes to edit | CRUD functionality is present on the user’s bag before payment is made – if the user wants to edit/delete their item, buttons are present for the user to perform this action in the bag view.
User error – what if it happens? | Toast messages appear on the site indicating to the user what has happened.
Information architecture | Using the tree structure with no more than 3 clicks for the user to reach a destination.

#### Skeleton Plane
Question |	Response for site design
-------- | ---------
How will the users get around? | Easy navigation for the user depending on their user status as mentioned above.
How will I present the content? | Following industry norms of the header -> content -> footer approach across all pages through the use of Django "extends" functionality.
How do I show relevant content? | By making the content audience appropriate as defined by the site user goals.
How do I structure the features and usability? | Non-registered user: Home/All products/Login/Create account navbar links and prompt buttons on the home page. Registered user: Home/All Products/Logout/Profile

#### Surface Plane
Question |	Response for site design
-------- | ---------
What is the visual language? |	Django extends as noted above. Colouring as per testing norms, layout is informative, Fonts as per media display standard, images/toast messages are clear and pop to the user, CTA buttons for site progression.
What is the economy? |	The most important user/owner elements are easily recognised
Readability and consistency |	Each site page is familiar to the user in terms of font/styling consistency

## Design Features

#### Wireframes
* Desktop wireframe - [attached](media/readme/wf-desktop-updated.pdf)
* Tablet wireframe - [attached](media/readme/wf-tablet-updated.pdf)
* Mobile wireframe - [attached](media/readme/wf-mobile-updated.pdf)

#### Typography
Lato is used as the main font on the site, as imported through Google Fonts. Sans-serif is used as the fallback font. According to an article on [perpetual media group](http://www.perpetualmediagroup.ca/tenbestfontsforprintandweb/):
_“The semi-rounded details of the letters give Lato a feeling of warmth, while the strong structure provides stability and seriousness.”_

Further, in this [blog post](https://www.justinmind.com/blog/best-google-web-fonts-website/), Lato is ranked as #1 on the “30 best Google Fonts for your website”. It is known that the designer of this font, Lukasz Dziedzic, _“created Lato to work transparently in body text and also to stand out individually when used in larger-sized titles”_.
With these descriptions in mind, Lato is used for the site design/accompanying text.

## Design & UX – How do they come together?

### User goals

User Goal | Feature(s)/ Content in response | Goal Met?
-------- | --------- | --------
(1)|	Colour/Font/Layout/Navigation/CTA structure. Responsive button elements and appropriate redirects/toast/CRUD messages. Clear call to action on user progression from site landing to purchasing item(s).|	Yes
(2)|	Displayed on the landing “home” page|	Yes
(3)|	Content of the home page displays clear CTA on which section the user should click. Further, Navbar links are split appropriately based on product category|	Yes
(4)|	Available in the navbar for non-registered/non-logged in users.|	Yes
(5)|	The use of toast popups and checkout success features provides feedback to users on edit/delete/checkout bag items.|	Yes
(6)|	Site is simplistic in nature as an online store - 3 click approach taken as noted in the UX section of this ReadMe. Search bar included in navbar|	Yes
(7)|	Django allauth templates are included in the project for use of their safety protocols|	Yes
(8)|	Any user can edit/delete bag items when they view their bag before checkout.|	Yes
(9)|	Stripe safety protocols and card processing is applied, allowing the user to securely checkout.|	Yes
(10)|	Cookie storage in the browser allows an individual to exit the site and reenter without the loss of any items in their bag.|	Yes
(11)|	All non-registered user CRUD functionality is present despite not having an account.|	Yes
(12)|	As per (3) above. Sort function present on all product pages|	Yes
(13)|	On sale section linked in the navbar. Further, all products that are on sale have a red pill image showing how much they are on sale, plus the percentage discount on the product. On checkout, the user is shown how much they are saving in euro by purchasing this on sale item.|	Yes
(14)| FAQ links are present at the bottom of each html page of the site.| Yes
(15)| Delivery costs are shown in both the bag, toast notifications and checkout views, as well as an indication of how much extra they should spend to ibtain free delivery.| Yes
(16)| A verified user can add a review and rating to a product if they havent already, and can see other reviews | Yes 
(17)| Site owners can add blog posts that allow all site visitors to view | Yes
(18)| Frequent vistor (1) - password functionality present on the login section of the navbar | Yes
(19)| Frequent vistor (2) - Ability to view past orders for registered users on their profile page on the navbar | Yes
(20)| Frequent vistor (3) - Present on the navbar | Yes
(21)| Frequent vistor (4) - Registered users can update their contact/delivery/billing details on the profile app, which feed directly into the checkout app for their next purchase | Yes

### Site owner/designer goals

Goal | Feature(s)/ Content in response | Goal Met?
-------- | --------- | --------
(1)|	Noted above.|	Yes
(2)|	Noted above.|	Yes
(3)|	Noted in the testing section of this file.|	Yes
(4)|	All 4 languages have been utilised in the creation.|	Yes
(5)|	Noted above.|	Yes
(6)|	Administrator access to manage all products/add a product/blog management/review management on the database present on superuser login.|	Yes
(7)| Use of django authorization, CSRF, Heroku, Stripe and secret key variables all ensure a secure site.| Yes

### Application features

##### Bootstrap Usage
The Bootstrap toolkit was used throughout including:

* Grid
* Navbar
* Buttons
* Toasts
* Cards
* Forms

##### Toasts

Bootstrap toasts were used to feedback to the user on success, information and error messages during product CRUD usage.

Successful:

![image](media/readme/success-toast.JPG)

Informational:

![image](media/readme/success-informational.JPG)

Error:

![image](media/readme/success-error.JPG)

As products are added/edited from the products/bag views, the corresponding toast message and cart reflect this change in status as shown:

![image](media/readme/toast-and-cart.JPG)

![image](media/readme/toast-and-cart2.JPG)

### Items on sale

The site superuser/owner can use their priviliges to select whether a product is on sale through the site management. They can set the percentage discount, and the updated product will then be included with other sale products from the respective view.
Each product on sale will have a Sale pill badge, original price with a strike through, sales price and arrow percentage discount in the product card.

See view of item on sale:

![image](media/readme/item-on-sale.JPG)

and the view where the superuser changes the boolean value with no sales price:

![image](media/readme/item-on-sale-post.JPG)

##### Bag/Checkout/Checkout success

The site has separate pages for bag, checkout and checkout success corresponding to each stage of the purchase process. The customer is able to alter the quantity in the cart between 1 and 99. The price for individual products, sub-total of quantity for each product, overall bag total and grand total after shipping cost (if applicable) is shown.

##### Checkout

Name, email, phone, address and card details are required on the checkout page.
A checkbox provides an option to save the contact and address details back to the profile.

![image](media/readme/checkout-profile-option-save.JPG)

##### Free shipping

A purchase below €100 will incur a 5% of order total shipping cost.
The shipping cose is waived for orders over €100.

##### Profile

Customer’s contact details and order history are saved in their profile. Contact details can be updated on the profile or check out pages.
Security is in place to ensure only the customer who submitted the order can see the order history.

![image](media/readme/profile-order-history.JPG)

##### Add/Edit/Delete products

A site owner can create new product for the Site Management link on the navbar. Existing products can be updated via the Edit and Delete links on each item in the product views.

Product editing (pre & post):

![image](media/readme/edit-product-1.JPG)

![image](media/readme/edit-product-2.JPG)

Product addition and subsequent deletion:

![image](media/readme/product-addition-1.JPG)

![image](media/readme/product-addition-2.JPG)

![image](media/readme/product-addition-3.JPG)

![image](media/readme/product-addition-4.JPG)

##### Search box

Full search capability on product titles and description.

![image](media/readme/searchbox.JPG)

and subsequent search for the term "barbell":

![image](media/readme/searchbox-2.JPG)

##### Order Success

Upon ordering, a customer will get a successful order message with a reference number. From their profile view (if registered and signed in), they will see this order as well as any previous orders they have made:

![image](media/readme/order-success-1.JPG)

![image](media/readme/order-success-2.JPG)

![image](media/readme/order-success-3.JPG)

##### Review Product

Site visitors can see can see reviews of products and what other people are saying about them.

See a product with two reviews and user has one:

![image](media/readme/review-2review.JPG)

See a product with two reviews and user has none:

![image](media/readme/review-2review-none.JPG)

See a product with no reviews:

![image](media/readme/review-noreview.JPG)

##### Blog posts

Site visitors can view detailed blog posts regarding fitness posted by the site owners.

See the blog page:

![image](media/readme/blog-view.JPG)

See the full blog post:

![image](media/readme/blog-full.JPG)

##### Footer Links

The footer of each page contains 3 clickable HTML files which the site user can view - FAQ, Contact Us and Shipping Info:

![image](media/readme/footer-help-links.JPG)

##### Defensive programming

* Confirm Deletion
* HTML validity
* Admin pages protected from non-admin access
* Errors 404 and 500 handled by pages within the site
* Comprehensive user notifications through toast/feedback loop noted

##### Crispy forms

Used to improve function and style of forms.

##### AWS S3 hosting

Static and media files hosted on AWS S3.

##### Responsive on all device sizes tested

The use of the Bootstrap grid system and additional media queries enables the site to display effectively on a broad range of desktop, tablet and mobile screen sizes. See the testing section of this file for further information on this. To note, the media queries present are:
* max-width: 1399px
* max-width: 991px
* max-width: 585px

### Future developments

There are a number of developments and rationale for these included below which I would like to implement into the site. However, given the time pressure I have decided to not include these in the final project.

Future development | Rationale
------------------ | ---------
Authentication email | Due to security restrictions on my laptop, I cannot sent a "confirmation email link" for users who sign up on the site. This is something I would ideally add as it would lead to verified emails and possibly a newsletter
A section allowing the users to purchase recommended items based on their interests | As the site would grow, having a related products app would benefit the site users - especially for users that are logged in
Varying product images for each product (side view/back) | Varying product carousel would enhance the UX for the user
Pagination | Not needed now, however if the site grew it would need pagination for the amount of products
Wish List | Decided not to include as I feel the category drilldown is effective, but should be added to a growing ecommerce site
Calculations for VAT & postage in different countries | Useful for non-Irish shipping

## Information architecture

### Site Logic and diagram
The site logic was developed using Python, Django, Json, Heroku, JavaScript and JQuery. Django templating language was utilised in the creation of the site.
See below "User Types and Permissions"/"CRUD Functionality" sections for more information.

See the [attached link](media/readme/site-logic-diagram.pdf) for a diagram of the site logic.

### User Types and permissions
There are three types of users that this website is designed for:

#### Visitor/Non registered User
A visitor is anyone who navigates to this website and can see home/products pages. Visitors can view the products, their narrative, add them to a cart with all CRUD functionality and checkout with an order number. They can see blog posts and review any product reviews of items. They can also register for an account/login with email verification.

#### Logged in User
A visitor who registers for an account automatically becomes a "user". Users have the same rights as visitors, plus they have access to their own profile where they can see all of their past orders and create their default profile information for checkout purposes. These users can change/forgot their password and log out. These users can add create a review for a particular product if they havent already.

#### Administrator/Superuser
Administrators have all the rights of a logged in user, but they also have the right to manage the information of all products in the store, as well as add a product. They can verify email addresses of users that wish to create an account. They can delete any user except themselves. This is a security feature so that an administrator doesn't accidentally delete their own account. They can also edit/add/delete blog posts and delete product reviews.

### CRUD Functionality

User type | Create |	Read |	Update |	Delete
-------- | --------- | -------- | -------- | --------
Visitor|	Yes|	Yes|	Yes|	Yes|
User|	Yes|	Yes|	Yes|	Yes
Admin|	Yes|	Yes|	Yes|	Yes

As seen in the table above referencing purchasing a product, all CRUD functionality is present in the application. However, some CRUD operations are restricted to particular user types - noted below.

#### Create

Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Account creation|Yes|Yes|Yes
Purchase a product|Yes|Yes|No
Password functionality|Yes|Yes|No
Blog post|No|Yes|No
Leave a review|Yes|Yes|No

#### Read
Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Home/Products Pages|Yes|Yes|Yes
User profile|Yes|Yes|No
Past orders|Yes|Yes|No
Manage/verify users|No|Yes|No
Blog post|Yes|Yes|Yes
Read a review|Yes|Yes|Yes

#### Update
Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Password|Yes|Yes|No
Bag items|Yes|Yes|Yes
Blog post|No|Yes|No

#### Delete
Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Account|Yes|No|No
Bag items|Yes|Yes|Yes
Manage users|No|Yes|No
Blog post|No|Yes|No
Item review|No|Yes|No

### Database model

See below for the database schema implemented in the file:

![image](media/readme/database-schema-updated.JPG)

## Technology and Languages used

### Languages

*	[HTML5](https://en.wikipedia.org/wiki/HTML5)
*	[CSS3](https://en.wikipedia.org/wiki/CSS)
*	[JavaScript](https://en.wikipedia.org/wiki/JavaScript)
*	[Python](https://www.python.org/)

### Frameworks, Libraries and Programmes

[jQuery](https://jquery.com/)

Used as part of JavaScript.

[GitHub](https://github.com/)

Used to store projects code upon Git push.

[Django](https://www.djangoproject.com/)

Site structure.

[Bootstrap 5](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

Used for templating and used in navbar/toasts/buttons/grid/breakpoints/lists and forms.

[Git](https://en.wikipedia.org/wiki/Git)

Used for version control through the Gitpod terminal and the Git add/commit/push action sequence.

[Microsoft Word](https://www.microsoft.com/en-ie/microsoft-365/word)

Used for designing of the wireframes as I am completing this project on my work laptop with no access to Balsamiq.

[Favicon](https://favicon.io/favicon-converter/)

Used to create the icons of the site.

[Font awesome](https://fontawesome.com/)

Used to add in the button icons throughout the site.

[Google fonts](https://fonts.google.com/)

Used to add the Lato font and related font weights to the CSS style file using the @import url function. To improve site load times, this file is loaded into the head element of the base HTML page and backed up by using sans-serif in CSS.

[Heroku](https://www.heroku.com/about)

A web hosting service that supports Python applications.

[Postgres](https://www.postgresql.org/)

Live database.

[AWS S3](https://aws.amazon.com/s3/)

Hosting live static and media files.

[JSON](https://www.json.org/json-en.html)

An open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs. Used for storing the attribute information for the products and categories of this file.

## Testing

<h1 align = "center">UPPPPDAAAAATE</h1>

See [link](static/rm_files/logic-diagram.pdf) for testing of the following areas:

* Code validation
* Accessibility testing
* Responsive testing
* Manual testing
* Testing user stories from User Experience (UX) section
* Known bugs


## Deployment

### Making a Local Clone

1. Log into GitHub and locate the Team_Lift_Sprint repository
2. Under the repository name, click ‘Clone or download’.
3. To clone the repository using HTTPS, under ‘Clone with HTTPS’, copy the link.

![image](media/readme/deploy-1-3.JPG)

4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in step 3:
$ git clone https://github.com/aryan008/team_lift_sprint

7. Click Enter. Your local clone will be created.

Please see this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for more detailed explanation.

8. Following Stripe documentation, create a Stripe account and in Developers on the API key tab find the public and secret key.
9. Also in Stripe create a Webhook and find the Webhook secret key.
10. Create an env.py file to contain the following environment variables.

![image](media/readme/deploy-1-10.JPG)

11. Create a .gitignore file ensuring pycache is added.

![image](media/readme/deploy-1-11.JPG)

12. Install all project requirements with the following command: pip3 install –r requirements.txt
13. Run database migrations with the following command: python3 manage.py migrate
14. Load category and product fixtures in following order:

![image](media/readme/deploy-1-14.JPG)

15. Create a superuser

![image](media/readme/deploy-1-15.JPG)

16. Run the app

![image](media/readme/deploy-1-16.JPG)

### Deploy to Heroku

1. Login to Heroku
2. Create new app

![image](media/readme/deploy-2-2.JPG)

3. Add name , choose closest region and click Create app

![image](media/readme/deploy-2-3.JPG)

4. In Resources create a new Postgres database

![image](media/readme/deploy-2-4.JPG)

5. Select Hobby Dev-Free plan and click Submit Order Form

![image](media/readme/deploy-2-5.JPG)

6. In your IDE install dj_database_url and psycopg2

![image](media/readme/deploy-2-6a.JPG)

![image](media/readme/deploy-2-6b.JPG)

7. Import dj_database_url in settings.py

![image](media/readme/deploy-2-7.JPG)

8. Replace default database with a call to dj_database_url.parse and give it the database URL from Heroku

![image](media/readme/deploy-2-8.JPG)

9. Run all migrations again for the Postgres database (see steps 11 to 13 in Making a Local Clone)
10. Install gunicorn to act as a webserver

![image](media/readme/deploy-2-10.JPG)

11. Freeze requirements

![image](media/readme/deploy-2-11.JPG)

12. Create a Procfile to tell Heroku to create a web dyno to run gunicorn to serve the Django app. This should contain the following:

![image](media/readme/deploy-2-12.JPG)

13. Login to Heroku from your IDE using your API key as the password

![image](media/readme/deploy-2-13.JPG)

14. Temporarily disable collectstatic so Heroku will not collect static files when we deploy- heroku config:set DISABLE_COLLECTSTATIC=1 --app team-lift-sprint

15. In Settings, create the following Config Vars

![image](media/readme/deploy-2-15.JPG)

16. Add the Heroku hostname to ALLOWED_HOSTS in settings.py

![image](media/readme/deploy-2-16.JPG)

17. Commit & push to GitHub
18.Initialise your IDE with Heroku and push to it.

![image](media/readme/deploy-2-18.JPG)

![image](media/readme/deploy-2-18b.JPG)

19. In Heroku on the Deploy tab select GitHub as Deployment method

![image](media/readme/deploy-2-19.JPG)

20. Search for respository and click Connect

![image](media/readme/deploy-2-20.JPG)

21. Click Enable Automatic Deploys

![image](media/readme/deploy-2-21.JPG)

### Configuring S3

1. Create an AWS account
2. Create a bucket for S3
3. Uncheck Block all public access and acknowledge settings

![image](media/readme/deploy-3-3a.JPG)

![image](media/readme/deploy-3-3b.JPG)

4. Enable static website hosting & Save changes.

![image](media/readme/deploy-3-4.JPG)

5. Add default values for index, error doc & click Save.

![image](media/readme/deploy-3-5.JPG)

6. In Permissions on CORS paste the following:

![image](media/readme/deploy-3-6.JPG)

7. Click Edit in Bucket policy to create a security policy

![image](media/readme/deploy-3-7.JPG)

8. Click Policy Generator and for Principal enter * and actions add Get Object

![image](media/readme/deploy-3-8.JPG)

9. Enter the ARN from step 7.
10. Click Add statement

![image](media/readme/deploy-3-10.JPG)

11. Click Generate Policy
12. Copy Policy JSON Document

![image](media/readme/deploy-3-12.JPG)

13. Paste into Bucket policy (with slash & asterisk at end of Resource for full access) & Save changes.
14. Click Edit in Access Control List, check box for List access for Everyone & Save changes.

![image](media/readme/deploy-3-14.JPG)

### AWS IAM (Identity & Access Management)

1. In AWS navigate to IAM, User groups, Create user group
2. Enter a name and click Create group

![image](media/readme/deploy-4-2.JPG)

3. In Policies, click Create Policy

![image](media/readme/deploy-4-3.JPG)

4. On the JSON tab, click Import managed policy

![image](media/readme/deploy-4-4.JPG)

5. Search for S3 and import the AmazonS3FullAccess policy

![image](media/readme/deploy-4-5.JPG)

6. Add in the ARN from the AWS Policy Generator page
7. Click Next Tags and Review

![image](media/readme/deploy-4-7.JPG)

8. Add a name, Description and click Create policy
9.Attach the policy to the group created.
10. In User Groups select your group
11. In Permissions, click Attach Policies

![image](media/readme/deploy-4-11.JPG)

12. Select the policy created & click Add permissions

![image](media/readme/deploy-4-12.JPG)

13. In Users, click Add users
14. Add username and Access Type as Programmatic access & click Next
15. Select to add user to our policy, click Next and Create User
16. Click Download.csv to get your access credentials.

![image](media/readme/deploy-4-16.JPG)

### Connect Django to S3

1. Install boto3

![image](media/readme/deploy-5-1.JPG)

2. Install Django Storages

![image](media/readme/deploy-5-2.JPG)

3. Freeze requirements

![image](media/readme/deploy-5-3.JPG)

4. Add the following settings for Django to connect to S3

![image](media/readme/deploy-5-4.JPG)

5.In Heroku Config Vars add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and delete the DISABLE_COLLECTSTATIC variable
6. In settings.py tell Django where static files are located

![image](media/readme/deploy-5-6.JPG)

7. Create a media folder on S3 and upload files

![image](media/readme/deploy-5-7.JPG)

8. Select Grant Public Read Access to the objects

![image](media/readme/deploy-5-8.JPG)
 
## Credits
### Content

* [Code Institute](https://codeinstitute.net/): Their sample [README.md](https://github.com/Code-Institute-Solutions/SampleREADME) was used as a design guide for my ReadMe file.
* The site was based on the Code Institute Boutique Ado project and as such the majority of django models/form/quanity javascript/sort functionality are based on this logic, however they are tailored to my project needs.
* Deployment notes - [Sneaker Dadi](https://github.com/thirdelement/sneaker-dadi): Their sample [README.md](https://github.com/thirdelement/sneaker-dadi#readme) was used as a guide for my ReadMe deployment section above.
* [Markdown help](https://guides.github.com/features/mastering-markdown/#) for this ReadMe documentation.
* Code Institutes [pre-installed gitpod repository](https://github.com/Code-Institute-Org/gitpod-full-template).
* Responsive image at the top of the ReadMe file is from [Am I Responsive](http://ami.responsivedesign.is/).
* Bootstrap 5: [Link](https://getbootstrap.com/docs/5.0/getting-started/introduction/).
* Inspiration for the project was taken from [mcsport.ie](https://www.mcsport.ie/).
* Stripe styling provided from Stripe website on the checkout form, including payment processing spinner.
* Blog class credit:
  - (1) - https://dev.to/madhubankhatri/blog-website-using-django-55ji - Madhuban Khatri
  - (2) - https://www.youtube.com/watch?app=desktop&v=GcqURKYfv00 - CodingWithMitch
* Credit for help on product review - https://www.youtube.com/watch?v=reFJ9hBLFUY - Coding Stuff

### Media
#### Attribute sources/links
* Products - The product images were taken either from [Rogue](https://www.rogueeurope.eu/?locale=en-GB) or [Mcsport](https://www.mcsport.ie/)
* Home page images from [Unsplash](https://unsplash.com):
  * Pitch - [Link](https://unsplash.com/photos/fDmpxdV69eA). Credit to Artist @thomascpark
  * Weightlifter - [Link](https://unsplash.com/photos/7kEpUPB8vNk). Credit to Artist @Anastase Maragos
  * Team Photo - [Link](https://unsplash.com/photos/6XUKomqujZM). Credit to Artist Alora Griffiths
  * Weight rack - [Link](https://unsplash.com/photos/uwk8IS-HfJ8). Credit to Artist @Rick Barrett

#### Font awesome
Link for font awesome “Button”/"Bag"/"Footer" icons: [Link](https://fontawesome.com/)

#### Favicon
Favicon creation at: [Link](https://favicon.io/favicon-converter/)

#### Google Fonts
Link for Google Fonts: [Link](https://fonts.google.com/)
 
### Code
 
* JSON Fixtures file help: From Code Institute
* Bootstrap Navbar: [Link](https://getbootstrap.com/docs/5.0/forms/form-control/)
* Support for creating the ReadMe file linked table of content: [here](https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents) and [here](https://www.setcorrect.com/portfolio/work11/)
* Support from @jo_ci and related CSRF error on django 4.0 update - [link](https://docs.djangoproject.com/en/3.2/ref/settings/#csrf-trusted-origins)

### Acknowledgements

* Tutor support at Code Institute for their support.
