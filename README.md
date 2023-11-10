# Maths Game - A Game to Practice Maths Equations

![responsive mock-up](assets/images/readme-images/mockup.png)

This is a game to make practicing math equations easy. The game allows the user to choose the kind of mathematical operation they would like to play with. After a set number of questions, here 5, the user gets feedback and can choose to play again or exit the game.

Visit the site [here](https://maths-game-dff2c71c7ebb.herokuapp.com/).

## Table of Contents

1. [Design](#design)
2. [Features](#features)
3. [UX](#ux)
4. [Testing](#testing)
5. [Sources](#sources)
6. [Credits](#credits)

## Design

All texts are kept short and simple to make them easy to read for the user.
Line breaks are used frequently to help the user visually separate different instructions, topics and questions.
No background images or colors other than what was provided with the CI template were used.

### Flowchart

The flowchart was created using [Lucid](https://lucid.app/users/login#/login). It gives a visual overview of the logical steps followed while playing the game. 

![Flowchart](assets/images/readme-images/flowchart.png)

## Features / Game Steps

The game follows a number of sequential steps.

- **Welcome Message**
    - Upon starting the game, a welcome message gets displayed.
    - It explains the goal of the game and how many rounds will be played.
    - Finally, it asks the user to enter their chosen name.

    ![Welcome Message](assets/images/readme-images/welcome-message.png)

- **Hero image**
    - The hero image was chosen as it depicts the Schönbrunn castle, one of Vienna's most famous sites. 
    - The relation to Vienna was deemed to be important as this is an English-language website targeted mostly at people located in Vienna. This way, people immediately get an association with Vienna even though the site is not in German language.
    - Also, for those with some more knowledge about psychoanalytics, Sigmund Freud, the "godfather of psychoanalytics" was from and mostly worked in Vienna. In professional circles, Vienna still has a very good reputation when it comes to producing good psychoanalysts/psychotherapists.
    - Since the rest of the site is quite calm and quiet, it was decided to keep the image at full opacity to make it pop.

    ![Hero image](assets/images/readme-images/hero-image.png)

- **Main section**
    - Subheaders on all pages give cues about the content of the individual parts.
    - Content varies depending on the page. 
    - Texts are kept short to help the user find information quickly.

- **Home page and call to action**
    - A picture of Dr. Himanshu Giri greets the user to give them a first impression of him. It is rounded for a softer look.
    - The welcome text gives the user a first understanding of what Dr. Giri offers.
    - Layout is vertical for smaller screens and horizontal to make good use of larger screens.
    - A call to action motivates the user to book a session. The button is a link which directs the user to the contact page.

    ![Home page including headshot of Dr Giri, welcome text and call to action](assets/images/readme-images/home-page-incl-headshot-text-and-call-to-action.png)

- **About page**
    - Images are related to the content they are associated with. They show pictures of various scenes which one might encounter in a therapy setting.
    - The information that site visitors will mostly look for is listed in clear list format, using bullet points where too many items make up the list.
    - Little icons give a playful vibe, giving lightness to heavy issues.
    - Layout is vertical for smaller screens and horizontal to make good use of larger screens.

    ![About page](assets/images/readme-images/about-page.png)

- **Contact page**
    - A form encourages visitors to leave their contact details for Dr. Giri to get in touch with them directly.
    - Should the site visitor choose to contact Dr. Giri themselves, they are provided with the address, email and phone details. The email address is provided as a link.
    - On larger screens, the contact information is displayed horizontally and separated into two columns for a cleaner look.

    ![Contact page](assets/images/readme-images/contact-page.png)

- **Footer**
    - The footer contains three icons which link to external social media sites.
    - The links open in new tabs, making it easy for users to come back to the site of Dr. Giri.
    - The footer is consistent throughout the pages.

    ![Footer](assets/images/readme-images/footer.png)

### Possible Future Features

- Include a video

    Dr. Giri has given a Ted Talk. I would like to embed this video directly on the about page.

- Improve the about page

    Make the costs on the about page into a table giving an easier overview to the site visitor.

- Give the user more options with the form

    I would like to give the site visitor the option to choose whether they would like to be contacted via email or via phone, and if phone, at which times.

## UX

### Site Goals

The site wants to attract people who face mental or psychological challenges in their lives and are looking for professional help from a qualified psychotherapist. Particularly, the site should speak to English- or Hindi-speaking people located in Vienna, or who would like to try psychotherapy online. 

### User Stories

**As a site visitor:**

- I want to confirm that Dr. Giri is a qualified psychotherapist.
- I want to know which languages Dr. Giri speaks.
- I want to learn about the types of sessions he offers.
- I want to know how much a session costs.
- I want to find out whether Dr. Giri specializes in the field which I struggle with.
- I want to see where Dr. Giri is located.
- I want to be able to get in contact with Dr. Giri in the manner that I choose to.
- I want to see a mobile-friendly layout and responsive design.

**As the site administrator:**

- I want to be able to easily update information such as pricing or location.
- I want to be able to add new content such as videos.

## Testing

- I confirmed that this project is responsive and looks good on various common screen sizes by using the devtools devices toolbar.
- I have confirmed that the form works and each field is required. There are error messages if a field is not filled out. If it is filled incorrectly, such as an @ missing in an email, or the phone number field containing letters, there are appropriate error messages.
- I confirmed that header and navbar are easily readable and understandable.

### Fixed Bugs

- Imported Google Fonts into html via <link>. This caused css-classes and -ids to not be applied. Fixed it by removing Google Fonts link from index.html and instead importing Google Fonts into style.css.
- Various flexbox styling problems. Fixed flexbox styling by applying differently colored borders to better understand the individual elements' behaviours. Border colors were removed after fixing the styling.

### Unfixed Bugs

- None.

### Validator Testing

- HTML ([W3C Validator](https://validator.w3.org/))
    - 3 errors found: two out of three errors were "section lacks heading". The other one was "The element ```a``` must not be a descendent of the `button` element."
    - Solution: introduced headings to the two relevant sections and set them to non-displayed. Styling the `a` as a button and removing the button element.

- CSS ([Jigsaw](https://jigsaw.w3.org/css-validator/))
    - 1 error found: "min-width too many values or values are not recognized: `none`".
    - Solution: removed min-width. It wasn't necessary anyways.

- Performance, Accessibility, Best Practices, SEO (Lighthouse Chrome Dev Tools)
    - Accessibility is at 100, which is what the focus was one.
Performance is mediocre, also after compressing images.
    - ![Lighthouse rating](assets/images/readme-images/lighthouse-report_project-1.png)

### Browser Testing (section adapted from Kay Welfare, results are my own)

**Layout:** Testing layout and appearance of site for consistency throughout browsers.

**Functionality:** Ensuring all links, navigation and form submit functions as expected throughout browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Edge        | ✔          | ✔             |
| Firefox     | ✔          | ✔             |
| Safari*     | only available to me on iPhone |
| IE          |deprecated by Microsoft, not tested|

*I asked my peers to review the site for me in Safari and one colleague came back with no bugs found (he made suggestions on styling which I did not implement since I considered them personal preference).

### Manual Testing (section adapted from Kay Welfare, results are my own)

| Feature     | Expect      | Action        | Result |
| :---------: | :----------:| :-----------: | :-----:|
| **Logo Icon**   | When clicked, home page will open   | Clicked Logo Icon  | Home page opened when clicked |
| **Navbar Buttons**  | When clicked, the respective page will open  | Clicked all individual navbar buttons | All respective pages opened when button was clicked |
| **Book A Session Now! Button** | When clicked, Contact page will open  | Clicked on the Book A Session Now! Button | Contact page opens |
| **Email link on contact page** | When clicked, a blank email will open with the email address as the recipient | Click email link | New blank email opens with email address as recipient |
| **Social link icons** | Social link icons open relevant websites in new tab when clicked | Click all individual icons | All respective sites open in new tab |
| **Form submit button** | Form submits when submit button is clicked | Fill out form and click submit button | CI form dump page opens and displays form contents |
| **Required form fields** | Form will not submit if required fields are blank and/or filled incorrectly, and fields will be highlighted and flagged | Fill out form incorrectly | Form does not submit and highlights incorrectly filled-in fields and gives prompts what may be wrong (eg @-sign missing in email address field) |

### Testing User Stories (section adapted from Kay Welfare, results are my own)

| Expectation                         | Result                          |
| :---------------------------------: | :------------------------------:|
| I want to confirm that Dr. Giri is a qualified psychotherapist | As a visitor, I can see that Dr. Giri is a psychotherapist on the home page, his full title is visible on the contact page |
| I want to know which languages Dr. Giri speaks | As a visitor, I can find the languages which Dr. Giri offers sessions in on the about page |
| I want to learn about the types of sessions Dr. Giri offers | As a visitor, I can find the types of sessions which Dr. Giri offers on the about page |
| I want to know how much a session costs | As a visitor, I can find the costs of the various types of sessions on the about page |
| I want to find out whether Dr. Giri specializes in the field which I struggle with | As a visitor, I can find the fields Dr. Giri specializes in on the about page |
| I want to see where Dr. Giri is located | As a visitor, I can find Dr. Giri's practice's address on the contact page |
| I want to be able to get in contact with Dr. Giri in the manner that I choose to. | As a visitor, I can choose to get in contact with Dr. Giri in the manner I prefer, whether this is to send an email, or call, or have Dr. Giri contact me |
| I want to see a mobile friendly layout and responsive design | As a visitor, I have a good view of the site on mobile device without overflow or side-scrolling |

## Deployment

This site was deployed on GitHub Pages:
- From the repository, first navigate to "Settings" (top of the page) and then "Pages" (left of the newly opened page)
- Under "Source" choose "Deploy from a Branch" in the dropdown menu
- Choose the "main" Branch, and folder "/(root)"
- Click "save"
- The website is subsequently deployed (this may take a few minutes) on GitHub Pages
- To get there, in the "Code" tab of the repository, on the right-hand side under "Environments" click on "github-pages"
- On the newly opened page, on the right-hand side, click on "View deployment"

## Sources

- Love Running walk-through project for basic structures of header and footer
- Favicon was generated using [favicon.cc](https://www.favicon.cc/)
- The mock-up image of the site on different devices was generated using [techsini.com](https://techsini.com/multi-mockup/)
- All images taken from pexels.com, except the headshot of Dr. Himanshu Giri, which is from author's private photos
- Images were compressed using [iloveimg.com](https://www.iloveimg.com/)
- Icons were taken from [fontawesome.com](https://fontawesome.com/)

## Credits
- Holly from Tutor Support for spotting a space in the import of my Google Fonts which caused problems with my styling
- https://css-tricks.com/dont-overthink-flexbox-grids/ for helping me figure out how to get the flexbox on my about page to produce same-width children
- https://www.w3schools.com/cssref/pr_list-style-position.php for helping me get the bullet points of my list inside the flex container
- Our group facilitator, Kay Welfare, for her patience and genuine efforts to help. And for not getting tired to repeat certain points over and over again
- Again, Kay Welfare, for sharing her readme with us
- https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_two_columns_flex for teaching me how to make two columns for the form
- https://sentry.io/answers/how-do-i-create-an-html-button-that-acts-like-a-link/ for helping me fix the error which came up in W3C testing that an ```a``` -element may not be the descendant of a ```button``` -element
- My mentor, Adegbenga Adeye, for his input
- My partner, Himanshu Giri, for providing me with the text input for this project


## Fixed bugs
- When writing the code I was trying to pass a variable into a method unsuccessfully. The problem was that I did not define the relevant variable, which was the outcome of another method, in the global space but only within that previous method. Solved by assigning the outcome of the previous method to a variable in the global space. 


## Credits
- On how to use the round() function: https://www.geeksforgeeks.org/round-function-python/