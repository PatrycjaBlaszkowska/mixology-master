# MIXOLOGY MASTER 

[Link to a live site](https://mixologymaster-15c467037ed9.herokuapp.com/)

![Responsive view of mixology master website](/docs/images/am-i-responsive.PNG)


## INTRODUCTION 

Welcome to my third project, part of the Code Institute Full Stack Development Course.
The main purpose of this project is to build a fully functioning, full-stack web application.

Mixology Master is a free-to-use cocktail recipe platform. 

The user can browse through available cocktail recipes without an account.
The user can also add their own recipes after registering and logging into their account.
All logged-in users can download a free guide on how to add their own recipe.

### Thank you for visiting Mixology Master!

## UXD – User Experience Design

A user experience designer, Jesse James Garrett, introduced five UX design elements in his book The Elements of User Experience.
In the book, he explains the steps of user experience projects and what UX designers should consider at each stage.
This is where most of my planning process steps came from.

The 5 planes of UX are as below:

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

## The Strategy Plane

### Creator Goals :

- As a creator, I want my webpage to be user-friendly.
- As a creator, I want my webpage to be fully responsive.
- As a creator, I want my webpage to be functional.
- As a creator, I want my webpage to be easy to navigate.
- As a creator, I want the purpose of my webpage to be clear.
- As a creator, I aim to foster repeat visits to my webpage from users.

### User stories :

**GUEST USER** :

- As a guest user, I expect the webpage to be easy to navigate.
- As a guest user, I expect the purpose of the website to be explained right away.
- As a guest user, I expect the registration process to be seamless and efficient.
- As a guest user, I anticipate being able to easily browse through recipes without the need to create an account.

**LOGGED-IN USER**

- As a logged-in user, I expect the webpage to be easy to navigate.
- As a logged-in user, I expect the login process to be seamless and efficient.
- As a logged user, I expect the user dashboard to include all important information and functions.
- As a logged user, I anticipate being able to add and manage my own recipes.
- As a logged user, I anticipate being able to delete my account.

**User stories are based on online research and my relatives experiance.**

## The Scope Plane

The planning process allowed me to prioritize the implementation of features based on their importance to my user stories, 
enabling me to identify which ones could be completed within the given deadline and which ones would need to be postponed for later implementation.

#### Features implemented upon webpage release :

- Introduction on the homepage providing information on the art of bartending.
- Page dedicated to recipes featuring all available recipes for users.
- Verification system for users.
- Ability for logged-in users to create and manage their own recipes.
- User-friendly navigation bar for easy access to different pages.
- Footer with links to social media platforms.
- Contact form for users to communicate with the website owner/admin.
- User dashboard for account management, recipe creation, and guide downloads.
- Search bar functionality to help users browse through a variety of available recipes.

#### Fatures planned to implement later :

- Two-step authentication.
- Password retrieval.
- Option for logged-in users to upload an image of the cocktail when submitting a recipe.
- Ability to search for cocktails based on available ingredients.

*Above decisions have been made based on below table.*

| Feature       | Feasibility   | Importance    |
| ------------- |:-------------:|:-------------:|
|Navigation     | 5             | 5             |
|Introduction   | 5             | 5             |
|Verification   | 5             | 5             |
|Recipes page   | 5             | 5             |
|Social media   | 5             | 5             |
|Dashboard      | 5             | 5             |
|Contact page   | 4             | 5             |
|Two-step auth  | 4             | 3             |
|Password retr. | 4             | 4             |
|Search bar     | 4             | 5             |
|Ingrid search  | 3             | 4             |

## The Structure Plane

### Colors :

#748D92 :

- Body background
- Buttons

![#748D92 Hex Color](./docs/images/748d92.PNG)

#FAFAFA :

- Text 
- Footer icons
- Links
- Buttons 
- User input (form)

![#FAFAFA Hex Color](./docs/images/fafafa.PNG)

#2E3944 :

- Navigation bar (background)
- Footer (background)
- Cocktail and user card (background) 
- View cocktail page (background)
- Specs page header (background)

![#2E3944 Hex Color](./docs/images/2e3944.PNG)

#000 :

- Delete modal (text) 
- Info section (background with opacity of 0.3)
- Contact form (background with opacity of 0.3)

![#000 Hex Color](./docs/images/000.PNG)

**Bootstrap default buttons colors** :

- #F8F9FA 

![#F8F9FA Hex Color](./docs/images/f8f9fa.PNG)

- #FFC107

![#FFC107 Hex Color](./docs/images/ffc107.PNG)

- #DC3545 :

![#DC3545 Hex Color](./docs/images/dc3545.PNG)

- #6C757D :

![#6C757D Hex Color](./docs/images/6c757d.PNG)


### Fonts :

**Roboto** :

- The choice of utilising the Roboto font from Google as the primary typeface was made due to its widespread popularity and user-friendly characteristics. With a focus on readability across various screen sizes, Roboto ensures an optimal user experience for all individuals accessing the content.

### Images :

Images for this project has been downloaded from : 

- [Gestational Diabates](https://www.gestationaldiabetes.co.uk)
- [Unsplash](https://unsplash.com/)
- [Pinterest](https://www.pinterest.co.uk/)

**More information in credits section.**

### Database

In my application, I'm storing the data about users and cocktails, which are related to each other through the 'user_id' foreign key in the 'Cocktail model'. By using a relational database, I can define these relationships between tables, ensuring data consistency and integrity. Using a relational database allows me to :

 - **Enforce data consistency** : 'Cocktail' model has a 'user_id' foreign key that references the 'id' column in the 'User' model. This foreign key ensures that every 'user_id' in the Cocktail table corresponds to a valid 'id' in the 'User' table.

 - **Maintain data integrity** : The 'user_id' column in the 'Cocktail' table uses 'db.ForeignKey("user.id", ondelete="SET NULL")'. This setup means that if a user is deleted, the 'user_id' in the Cocktail table will be set to 'NULL' instead of leaving orphaned entries. This approach maintains referential integrity by not leaving 'user_id' values that do not correspond to any user.

 - **Facilitate querying and filtering** : The foreign key relationship allows to perform efficient joins between the 'User' and 'Cocktail' tables. For example, admin can easily retrieve all cocktails created by a specific user or list all cocktails and their associated users.

**Database model diagram** :

![Database model diagram](./docs/images/database-diagram.PNG)

## The Skeleton Plane

As part of an ongoing effort to continually improve the project, I identified a number of key features that were previously missing and were negatively impacting the overall user experience. In order to address this, I implemented several significant changes to the project, aimed at enhancing usability and functionality.

**SIGIFICANT CHANGES ACROSS ALL WIREFRAMES** :
- In an effort to improve the overall user experience and simplify the layout of the page, I have made the decision to relocate the login and register buttons from their previous position below the navbar to the navbar itself.This change was motivated by feedback that the original placement was causing the page to appear cluttered and overwhelming. By integrating these buttons into the navbar, we can streamline the design and provide a more intuitive and user-friendly interface.
With this change, users will now have easy access to login and registration functionality directly from the main navigation bar without having to scroll down to a separate section. This update aims to enhance the overall usability and aesthetic appeal of the page, making it more appealing to users.

- Once a user logs in, the "Login" and "Register" buttons in the navbar are replaced with the "Dashboard" and "Logout" buttons. This change aims to provide a more personalised and streamlined experience for authenticated users. By providing a direct link to the dashboard, users can quickly access their personalised content and features without having to navigate through the application. Additionally, the "Logout" button offers a convenient way for users to sign out of their account when they are finished using the application. This update enhances the overall user experience by providing a more intuitive and contextual navigation menu that adapts to the user's login state.

[Recipes Page wireframes](./docs/wireframes/recipes-page.pdf)

- To enhance the discoverability of the webpage's extensive cocktail collection, I have added a cocktail category filter to the recipes page. This feature allows users to browse our selection of cocktails by their preferred alcohol type. By filtering by category, users can quickly find cocktails that match their taste preferences and interests.
I also optimised the layout of the webpage's cocktail display to provide a more streamlined and visually appealing experience. To achieve this, we have reduced the number of cocktails displayed in each row from 4 to 3. This change allows for a more balanced and harmonious layout, making it easier for users to focus on the featured cocktails and their descriptions. With this update, users can enjoy a more enjoyable browsing experience and discover new favourite cocktails with ease.

[Dashboard Page wireframes](./docs/wireframes/dashboard-page.pdf)

- I optimised the layout of the webpage's cocktail display to provide a more streamlined and visually appealing experience. To achieve this, we have reduced the number of cocktails displayed in each row from 4 to 3. This change allows for a more balanced and harmonious layout, making it easier for users to focus on the featured cocktails and their descriptions. With this update, users can enjoy a more enjoyable browsing experience and discover new favourite cocktails with ease.

- I decided to introduce a new Account Management section. This feature allows users to take control of their account settings and customise their experience on Mixology Master.
With this new section, users can now update their username, which provides an opportunity to personalise their identity on our platform. Additionally, I have added the ability to delete an account, giving users more control over their online presence and allowing them to easily remove their information from the database.

### ADDITIONAL PAGES :

**Unplanned Feature Addition: Account Management**

- During the development process, I introduced an unforeseen feature addition to the platform: the Account Management section on the user's dashboard. This section allows users to update their username and delete their account, providing an opportunity for them to personalise their identity on the platform. The page redirects to the new HTML page when the user changes their name. This change was not part of the original plan, and therefore, I did not create wireframes for this page.

![Account Management section on user's dashboard](/docs/images/edit-username.PNG)

**New User Interface: Dashboard and Admin Panel**

- In addition to the Account Management section, I also made significant changes to the user's dashboard and introduced an admin panel. The user's dashboard has been split into two separate sections: the user's new account management section and a "My Recipes" section, which displays a list of recipes they have added to the platform. The admin panel, on the other hand, allows administrators to manage all added recipes, including creating, editing, and deleting recipes. Due to these changes, I did not create wireframes for this page as it was not part of the original design plan.

![Admin panel - new page](/docs/images/admin-panel.PNG)

## The Surface Plane

### Features present across the project :

### Navigation bar :

The navigation bar is a persistent feature on every page and has been designed to be fully responsive, ensuring an optimal user experience across all devices and resolutions. On mobile devices, the navigation bar automatically transitions to a hamburger menu, providing easy access to all additional pages and sections. This intuitive design enables users to navigate the site with ease, regardless of their device or screen size.

**Desktop** :

![Navbar - desktop view](/docs/images/navbar-desktop.png)

**Mobile** :

![Navbar - mobile view(hamburger)](/docs/images/navbar-mobile-hamburger.png)

![Navbar - mobile view](/docs/images/navbar-mobile.png)

### Footer :

The footer is a consistently present element on every page, featuring a comprehensive design that is fully responsive and adaptable to all devices and screen resolutions. Additionally, the footer includes a section dedicated to social media links, which open in a new tab when clicked, allowing users to seamlessly engage with the organisation's online presence without disrupting their navigation experience.

![Footer - mobile & desktop view](/docs/images/footer.png)

### Hero image :

The hero image is strategically featured on the home page to immediately capture the user's attention and effectively communicate the purpose of the website. To ensure an optimal user experience, the hero image is designed to be responsive, seamlessly adapting to different screen sizes and devices. This means that users viewing the website on desktop computers will see a distinct hero image, while mobile device users will be presented with a tailored version that is optimised for their smaller screen size and mobile-specific navigation needs.

**Desktop** :

![Hero image - desktop view](/docs/images/hero-img-desktop.png)

**Mobile** :

![Hero image - mobile view](/docs/images/hero-img-mobile.png)


### Introduction section :

The introduction section of the website is designed to quickly convey the purpose and essence of the platform, allowing users to assess whether it is suitable for their interests within a brief timeframe. Following this initial section, a visually appealing divider image featuring a selection of fresh and tasty cocktails is prominently displayed. However, in consideration of mobile device users, this image is strategically hidden from view to prevent clutter and ensure an unobstructed user experience on smaller screens, ensuring that the content remains easily accessible and readable.

![Introduction section](/docs/images/introduction-section.png)

### Information section :

The "What's a Cocktail Spec?" and "Is a Bartender Kit Needed?" sections of this website provide valuable information for users looking to explore the world of cocktail-making. The "What's a Cocktail Spec?" section explains the concept of a cocktail specification, which is a detailed and precise recipe that includes the exact measurements of each ingredient, a specific type and brand of alcohol or mixer, the preparation method, and any garnishes or finishing touches. The "Is a Bartender Kit Needed?" section addresses the importance of having a basic bartender kit, which typically includes essential tools such as a shaker, jigger, strainer, muddler, and bar spoon. This information aims to educate users on the importance of accuracy and efficiency in cocktail preparation and provides guidance on how to get started with their own bartending journey.

![Information section](/docs/images/information-section.png)


### Recipes Page - header :

The Recipes page header section provides an overview of the purpose of this page, which is to showcase a curated collection of cocktail specifications (specs) for users to explore and create their own unique drinks. For logged-in users, this section also includes a feature to add their own cocktail spec, allowing them to contribute to the community and share their creations with others. This feature enables users to upload their own recipe, complete with measurements, ingredients, and preparation methods, making it easy to share and discover new cocktails with like-minded enthusiasts.

![Recipes page header](/docs/images/recipes-page-header.png)

### Filter and Search bar :

The "Alcohol Type Filter" and "Search Bar" features enable users to quickly and easily discover the perfect cocktail recipe. The "Alcohol Type Filter" allows users to narrow down their search by selecting from a range of spirits, such as gin, whisky, rum, or vodka, to find cocktails that feature their preferred base spirit. The "Search Bar" enables users to search for cocktails by name. By combining these two features, users can rapidly locate and explore a vast array of cocktail recipes, making it easy to find the perfect drink to suit their taste preferences. On mobile devices, the "Alcohol Type Filter" toggles to the icon for easy access, allowing users to quickly switch between different spirit options without having to navigate through multiple menus.

**Desktop** :

![Filter and Search - desktop view](/docs/images/filter-and-search-desktop.png)

**Mobile** :

![Filter and Search - mobile view](/docs/images/filter-and-search-mobile.png)


### Cocktails section :

The cocktails section displays a collection of cocktail recipes, each presented in a visually appealing card format. The cards feature a cocktail icon, the drink's name, category, and description, as well as a brief summary of its ingredients and characteristics. Each card is linked to a detailed view of the cocktail, where users can learn more about its ingredients, preparation instructions, and other details. This section allows users to browse through a variety of cocktails and discover new recipes to try.

![Cocktails section](/docs/images/cocktails-section.png)

### Contact us section :

This contact form is designed to provide a convenient way for users to get in touch with admin. The form allows users to submit their name, email address, and message.

![Contact us section](/docs/images/contact-us.PNG)

### "Thank you" / confirmation page :

This page serves as a confirmation of successful contact submission, displaying a friendly message to acknowledge receipt of the user's inquiry. The page provides a brief update on our expected response time, ensuring transparency and setting realistic expectations. A convenient 'Take me back!' button allows users to easily navigate back to the homepage, where they can continue exploring the platform or initiate a new contact request if needed. This page provides a seamless and user-friendly experience, ensuring that users feel valued and informed throughout the communication process.

![Thank you / confirmation page](/docs/images/thank-you-page.PNG)

### Register section :

The registration page allows users to create a personal account, giving them access to a secure area where they can manage their own cocktail recipes. Upon registration, users can choose a unique username and password, which will serve as their credentials for logging in to the platform.

![Register section](/docs/images/register.PNG)

### Login section :

The login page allows users to log into their personal account, giving them access to the user dashboard. By logging in, users can take ownership of their cocktail creations and enjoy a more personalised experience on the platform.

![Login section](/docs/images/login.PNG)

### Dashboard - account management section :

This feature allows users to take control of their account settings and customise their experience on Mixology Master. With this new section, users can now update their username, which provides an opportunity to personalise their identity on our platform. Additionally, the user has the ability to delete an account, giving them more control over their online presence and allowing them to easily remove their information from the database.

![Dashboard - account management](/docs/images/account-management.PNG)

### Edit username section / page :

This page / feature allows users to modify their existing username, providing an opportunity to refresh their online identity or correct any typos. By filling out the updated information, users can submit their new username and save the changes. To ensure a seamless experience, this page includes checks to guarantee that the chosen username is unique and available for use, preventing any potential conflicts or duplicates. With this update feature, users can easily customize their account details and maintain a consistent online presence.

![Edit username page](/docs/images/edit-username.PNG)

### Dashboard - cocktail management section :

The 'My Recipes' section is a personalised space where users can curate and manage their own collection of recipes, adding new ones, editing existing ones, and deleting any that are no longer needed. This feature allows users to easily access and organise their favourite recipes, making it simple to revisit and experiment with different flavours and combinations. Additionally, users can also access a complimentary guide on how to create effective recipes.

![Dashboard - cocktails management](/docs/images/cocktail-management.PNG)

### Add cocktail page :

The 'Add Cocktail' page allows users to create and submit their own unique cocktail recipes to their personalised 'My Recipes' section. Users can fill out a form providing essential details such as cocktail name, description, and category (by selecting from a list of available alcohol types). Additionally, users can specify ingredients and prep instructions, allowing them to capture every detail of their recipe. Once the form is submitted, the new recipe will be added to their 'My Recipes' section, making it easily accessible and available for viewing on their dashboard.

![Add cockail page](/docs/images/add-cocktail.PNG)

### Edit cocktail page :

The 'Edit Cocktail' page is where users can refine and customise their cocktail recipes by making changes to the essential details. Users can update the recipe name and description and add or modify the ingredients and preparation instructions. They can also select the type of alcohol used in the recipe, ensuring accurate categorization and discovery by other users. Once saved, the updated recipe will be reflected on the recipes page and the user's dashboard.

![Edit cockail page](/docs/images/edit-cocktail.PNG)

### Admin panel :

The admin panel allows administrators to manage all added recipes, including creating, editing, and deleting recipes.

![Admin panel](/docs/images/admin-panel.PNG)


## Technologies used :

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript)
- [Python](https://developer.mozilla.org/en-US/docs/Glossary/Python)
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Jest](https://jestjs.io/)
- [jQuery](https://jquery.com/)
- [Gitpod](https://www.gitpod.io/)
- [Github](https://github.com/)
- [Git](https://git-scm.com/)
- [Bootstrap](https://getbootstrap.com/)
- [FontAwsome](https://fontawesome.com/)
- [Balsamiq](https://balsamiq.com/wireframes/?gad_source=1&gclid=Cj0KCQiAy9msBhD0ARIsANbk0A_UrgDIhg_KSUHNCOUn-D9DiHl_9Z1dwScGRuI4JET1bnKbQkqwSb8aArFqEALw_wcB)
- [Google Fonts](https://fonts.google.com/)
- [QuillBot](https://quillbot.com/)
- [Google Developer Tools](https://developer.chrome.com/docs/devtools/)
- [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)

## Testing :

### User stories :

[User stories testing](/docs/testing/testing.md)

### Automatic Testing(Jest) :

As part of testing protocol, all functions have undergone a thorough examination using Jest, a popular JavaScript testing framework. Each function has been carefully written and tested to ensure it meets the expected behavior and functionality requirements.

![Jest tests results](/docs/images/jest-tests.PNG)

### Manual Testing :

- Navigation bar :
    - Navbar remains fully responsive across all devices and resolutions. 
    - On mobile devices, the navigation bar successfully transitions to a hamburger menu.
    - All links are working as expected.

- Footer :
    - Footer remains fully responsive across all devices and resolutions. 
    - All links are working as expected.

- Buttons :
    - All buttons across pages are working as expected.
    - Buttons remain fully responsive across all devices and resolutions.

- Grid system(Bootstrap) :
    - Grid system is working as intended successfully changing amount of collumns on smaller devices making website fully responsive.

- Filter section :
    - The category filter efficiently fetches categories from the database and allows users to filter cocktails based on their chosen alcohol type.
    - The user-friendly search bar quickly and accurately returns results, making it simple for users to find their desired cocktails by name.

- Cocktails section :
    - "Read" button is working as expected.
    - The cocktail name on each recipe page, which is also a clickable link, allowing users to quickly jump back to the search results page and explore other related cocktails, is working as expected.

- Adding new cocktail :
    - Upon submitting the form, the entered cocktail details are successfully stored in the database, enabling users to view and explore their newly created recipe on relevant pages.

- Editing existing cocktail :
    - Upon submitting the form, the updated cocktail details are successfully stored in the database, enabling users to view changes made to the recipe on relevant pages.

- Register form :
    - The registration process successfully adds the user to the database, providing them with secure login credentials and access to premium features and content.

- Login form :
    - Upon submitting the form, the user is successfully redirected to the user's dashboard, where they gain access to premium features and content.

- Contact form :
   - Upon submitting the form, the user is successfully redirected to the confirmation page.

- Delete feature :
    - After confirming the deletion, the user's account or cocktail is successfully removed from the database.

- Change username form :
    - Upon submitting the form, the updated username is successfully stored in the database and reflected on the user's dashboard.

- Logout :
    - The logout button effectively logs the user out of the system, securely ending their session and clearing all authentication data.

### Devices used during testing :
- Desktop PC
- Laptop 
- Lenovo Tab M10 Plus
- Iphone

### Chrome Dev Tools :

The project's responsiveness was thoroughly tested using Chrome Dev Tools, which allowed for precise debugging and optimisation. 
The Responsive Viewer browser extension was used to emulate the following devices :

- Iphone SE
- Iphone XR
- Iphone 12 Pro
- Iphone 14 Pro Max
- Pixel 7
- Pixel 2 
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- Samsung Galaxy Note20
- iPad Mini
- iPad Air
- iPad Pro
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Asus Zenbook Fold
- Samsung Galaxy A51/71
- Nest Hub
- Nest Hub Max
- Fire HD 10
- Pixelbook Go

![Responsive viewer - part one](/docs/images/responsive-viewer-first.PNG)
![Responsive viewer - part two](/docs/images/responsive-viewer-second.PNG)

### Validation :

[HTML validator](https://validator.w3.org/)

- 0 warnings
- 0 errors

![HTML validator results](/docs/images/html-validator.PNG)

[CSS validator](https://jigsaw.w3.org/css-validator/)

- 0 warnings
- 0 errors

![CSS validator results](/docs/images/css-validator.PNG)

[JS validator](https://jshint.com/)

- 0 errors
- 0 warnings
- One undefined variable - "module" :
module.exports has been used to export js functions in order to test them with Jest. As per [freeCodeCamp](https://www.freecodecamp.org/news/module-exports-how-to-export-in-node-js-and-javascript/) the syntax is valid. Using if (typeof module === 'object') removed the error from the console but not from the JSHint.

### Bugs and Fixes :

- Footer wasn't fixed at the bottom of the page :
    - Fixed by using [::after](https://developer.mozilla.org/en-US/docs/Web/CSS/::after) pseudo-element element on body and set it to the same height as footer.

## Deployment 

The master branch of this repository is the most current version and has been used for the deployed version of the site.
The Code Institiue student template was used to create this project.

[Code Institute Template for Gitpod](https://github.com/Code-Institute-Org/gitpod-full-template)

1. Click **Use This Template** button.
2. Give your repository a name, and description.
3. Open [Gitpod EDI](https://www.gitpod.io/) and log into your account.
4. Click **New Workspace** button.
5. Create a workspace from your project repository by creating a clone.

### Creating a clone :

1. From the repository, click **Code**.
2. In the **Clone >> HTTPS** section, copy the clone URL for the repository.
3. Paste a link into the designated area on the Gitpod.

### Forking :

1. From the repository, click **Fork**.
2. Give your repository a name.
3. Click **Create fork**.
