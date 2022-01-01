<h1>Testing Section</h1>

As per the table of contents, the following areas of testing were reviewed:

* Code validation
* Accessibility/Lighthouse testing
* Responsive testing
* Manual testing
* Testing user stories from User Experience (UX) section
* Known bugs

### Code validation
The W3C Markup Validator, W3C CSS Validator, JSHint JavaScript Validator Services and PEP8 online were used to validate the project to ensure there were no errors in the project. 

##### W3C CSS Validator

See the below screenshot for W3C CSS validation, with no errors present:

![image](media/readme/css-validator.JPG)

##### W3C Markup Validator

In using the W3C markup validator, a number of non-fixable errors were present through the validation process. See below explanations for error explanation.

1) Header error

The head element is deemed to be missing the child element "title". This is present on the base.html page, however this error results where base.html is extended and as such the validator has not picked it up. No further edits required.

![image](media/readme/head-error.JPG)

2) Spacing error

W3C noted that there are non-space characters inside a table. This is present on any templated language "for" loops, whereby a html tag is not present on either side of these statements. No further edits required due to python language used in HTML templates.

![image](media/readme/spacing-error.JPG)

3) URL error

This refers to the use of "{}" url references throughout the HTML pages. These braces are used for site references and again, due to django language site navigation. No edits required.

![image](media/readme/url-error.JPG)

4) Sort error

The below three errors are present on the HTML pages where the sort function is used. Python language "if" statement is present on the user interactive sort statement and possible through the use of python logic. No edits necessary.

![image](media/readme/sort-error.JPG)

As above explanations, these are not true errors but due to the templating language present in Django/Python language. HTML validation showed no further errors and as such this project has passed this testing protocol.

##### JSHint JavaScript Validator Services

See below screenshots for results on JSHint validation on seperate JS code (3) - no errors present:

![image](media/readme/countryfield-js-checker.JPG)

![image](media/readme/sort&jump-js-checker.JPG)

![image](media/readme/stripe-js-checker.JPG)

##### PEP8 online
<h1>UUUUPPPPDAAAATE</h1>

### Accessibility/Lighthouse testing

[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used on all pages to review site accessibility. No errors on the site occurred as a result of this accessibility testing.

See below for results on various pages:

* Home Page

![image](media/readme/home-page.JPG)

* Products Page

![image](media/readme/products-page.JPG)

* Bag Page

![image](media/readme/bag-page.JPG)

* Checkout Page

![image](media/readme/checkout-page.JPG)

* Profile Page

![image](media/readme/profile-page.JPG)
