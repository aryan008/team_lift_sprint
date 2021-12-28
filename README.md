<h1 align = "center">Team Lift Sprint</h1>

View the live project at the following [link](https://adam-team-lift-sprint.herokuapp.com/).

<h1 align = "center">UPPPPDAAAAATE</h1>![See how the site looks across the devices](static/rm_files/responsive.PNG)

Team Lift Sprint is an online shopping site that sell a manner of goods related to sport and/or sporting equipment. It is designed for Strength & Conditioning coaches, team managers, players and those focusing on getting the best out of their performance. The website provides status and feedback to users at all stages of the shopping process, as well as items on sale and correct UX design. Coming from a sporting background myself, the site itself comprises a number of categories which are discussed in detail below with the aim that Team Lift Sprint be a "one stop shop" for all those either training individually or in a group.

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
   5.	[Surface plane](#surface-plane)
   6.	[Breakdown of site design](#breakdown-of-site-design)
   
  *	[Who/ What/ How](#who-what-how)
  *	[User stories](#user-stories)

* [Design Features](#design-features)
  1. [Wireframes](#wireframes)
  2.	[Typography](#typography)
  3.	[Database model](#database-model)
  4.	[Imagery](#imagery)
  5.	[Features implemented](#features-implemented)
  6.	[Features left to implement](#features-left-to-implement)

* [Design & UX – How do they come together?](#design--ux--how-do-they-come-together)
  * [User goals](#user-goals)
  * [Site owner/designer goals](#site-owner/designer-goals)

* [Information Architecture?](#information-architecture)
  *	[Site Logic and diagram](#site-logic-and-diagram)
  *	[User Types and permissions](#user-types-and-permissions)
  *	[CRUD Functionality](#crud---create-read-update-and-delete)
  *	[Mongo DB Database Structure](#mongo-db-database-structure)

* [Technology and Languages used](#technology-and-languages-used)
  *	[Languages](#languages)
  *	[Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)

* [Testing](#testing)
  * [Code validation](#code-validation)
  * [Accessibility testing](#accessibility-testing)
  * [Responsive testing](#responsive-testing)
  * [Manual testing](#manual-testing)
  * [Testing user stories from User Experience (UX) section](#testing-user-stories-from-user-experience-ux-section)
  * [Known bugs](#known-bugs)

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
6.	Easy navigation of the site
7.	Built-in safety protocols – user authentication, appropriate redirects, site action feedback
8.	The ability to edit/delete any items in my bag
9.	Secure card payment protocols
10.	Ability to view my checkout items if I have accidentally exited the site
11.	Buy an item without registering
12.	Browse products easily
13.	View and purchase whats on sale
14.	Have a FAQ section where I can get in touch with the company regarding shipping/delivery, etc.


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
A split of products based on what the user is looking for - themselves/team/indoor/outdoor | 3 | 5
Footer links include FAQ's that is standard across all ecommerce sites | 4 | 5
Varying product images for each product (side view/back) | 3 | 3
Integration of secure payment system | 5 | 5
Pre paying the user has the ability to edit their bag items | 5 | 5
Sort functionality on all product views | 3 | 5
Products on sale are clearly defined and shown how much the user saves by purchasing | 4 | 5
