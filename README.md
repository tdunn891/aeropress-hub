# Milestone Project 3 - [AeroPress Hub](https://aeropress-hub.herokuapp.com/)

## Contents

1. [**Project Purpose**](#project-purpose)

2. [**UX**](#ux)

   - [**Strategy**](#strategy)
   - [**Scope**](#scope)
   - [**Structure**](#structure)
   - [**Skeleton**](#skeleton)
   - [**Surface**](#surface)
   - [**User Stories**](#user-stories)

3. [**Features**](#features)

   - [**Existing Features**](#existing-features)
   - [**Features Left to Implement**](#features-left-to-implement)

4. [**Database**](#Database)

5. [**Technologies Used**](#technologies-used)

6. [**Testing**](#testing)

   - [**Heroku**](#heroku)
   - [**Local Deployment**](#local-deployment)

7. [**Deployment**](#deployment)

8. [**Credits**](#credits)

   - [**Content**](#content)
   - [**Media**](#media)
   - [**Acknowledgements**](#acknowledgements)

## Project Purpose

AeroPress Hub was developed to centralise and showcase AeroPress coffee brews, from both champion baristas and AeroPress enthusiasts. Users can share their own as well as edit or delete existing brews. The application caters to the passionate global community that exists around this humble yet iconic brewer.

## UX

### Strategy

Site Objective: Provide platform for AeroPress enthusiasts to find and share AeroPress recipes

User Needs: Contribute, view, edit, and delete brews

Opportunities/Problems table used to determine the strategic priorities UX efforts should address (in this order):

| Opportunity/Problem                                                 | Importance | Viability/Feasibility |
| ------------------------------------------------------------------- | :--------: | :-------------------: |
| A. Centralise AeroPress recipes                                     |     5      |           5           |
| B. Allow contributions, edits, and deletion of brews                |     5      |           5           |
| D. Provide graphs and statistics of previous World AeroPress Champs |     2      |           4           |
| E. Encourage AeroPress purchases via affiliate links                |     1      |           2           |

### Scope

#### Functional Specifications

In considering functional specifications, I researched existing coffee recipe sites, including the AeroPress official website, and the World AeroPress Championship website and Android applications such as Brew Timer. This helped to identify the key data fields and features users of coffee applications expect to see.

Feature Set:

- Brew Browser: Filterable, sortable table of communal dataset of brews from World AeroPress Champions and regular user brews.
- Add Brew: Ability to add brew to communal data set
- Edit Brew: Ability to edit any field
- Delete Brew: Ability to delete any brew
- About Page: To find out more about the competition

#### Content Requirements

In order to provide the value of the above features, the following content is required:

- MaterializeCSS 'collapsible' collection
- Checkboxes for filtering
- Dropdowns for sorting and for form input (Add & Edit)
- MaterializeCSS range sliders for form input (Add & Edit)

### Structure

#### Interaction Design

Consistency & Predictability:

- A consistent coffee colour scheme and navigation bar is present throughout the site
- On smaller devices, navigation links collapse into 'burger' button

Feedback:

All interactive elements provide feedback to the user to encourage interaction and provide confirmation when actions are taken.

- Checkbox labels change colour on hover.
- Sort by dropdown has border transition on hover.
- Each record in the table changes background colour and cursor on hover.
- 'Like' button changes colour on hover.
- Icons: medal, timer, water temp provide tooltip additional information on hover.
- Navigation links change colour on hover.
- Pagination links (including chevrons) have background colour change on hover.
- All buttons have border transition on hover.
- All buttons have wave effect on click.
- Form validation exists in Add & Edit pages for relevant fields - field displays red 'Required' if invalid, green if valid.
- 'Toast' messages are briefly displayed to show confirmation of these user actions - Brew Added, Brew Updated, Brew Deleted, Brew Liked.

#### Information Architecture

The filtering and sorting panel is located on the left of the brew table (on desktop devices), a logical and intuitive position expected by users.

Pagination was implemented in the Brew Browser, showing only 8 brews at a time in order prevent cognitive overload. Pagination ensures that the sorting and filtering panel is easily reachable, particularly on mobile devices. The relatively small amount of records (~40) lends itself to pagination, as only a handful of pages are needed to hold all records. As the number of records grows, the records per page could be increased.

The Add Brew and Edit Brew pages are on their own pages for two main reasons: 1. The form features a significant amount of fields (10), which requires a sufficient amount of the viewport. 2. There is no benefit derived from viewing the Brew Browser at the same time while Adding a Brew. In the case of Edit Brew, the form fields are all prefilled (including range sliders) with the brew's current values.

### Skeleton

#### Wireframes

Two sets of wireframes were created in the early development stage to inform the structure and layout for different device sizes.

[Desktop & Mobile Wireframes](https://github.com/tdunn891/milestone-3/tree/master/static/images/wireframes)

### Surface

Colours: Coffee Brown (#4a2c2a) was chosen as the dominant colour across the site for obvious reasons.

Background Image: The coffee beans background image is immediately engage the user. The image covers only the lower portion of the viewport to ensure that it doesn't distract from the main content.

Other Images: The image with four hands holding AeroPress components was selected to give a feeling of community and encourage sharing of brews.

Fonts: A playful font ('Montserrat') was selected to emulate the fun nature of the World AeroPress Championships.

### User Stories

User stories:

- User 1 - "As a user who has just bought an AeroPress but doesn't know how to use it, I want to see how the champion baristas use it."
- User 2 - "As a user who has discovered an innovative new way to brew with the AeroPress, I want to share it with the community."
- User 3 - "As a user who is interested in analysing what makes a gold medal brew, I want to be able to hone in on these brews."
- User 4 - "As a user who has just purchased a metal filter and producing poor results, I want to see the community's most popular metal filter brews."
- User 5 - "As a user who has tried a recipe submitted by another user, I want to be able to edit (improve) it for the benefit of other users."
- User 6 - "As a user who loves high coffee dosages, I want to sort the dataset by dosage."

How their needs are met:

- User 1's needs are met by the ability to browse through champion brews with detailed steps
- User 2's needs are met by the ability to share a brew via the Add Brew page
- User 3's needs are met by the ability to filter by Place: Winners First
- User 4's needs are met by the ability to filter by metal filter and sort by 'Most Popular'
- User 5's needs are met by the ability to Edit a brew
- User 6's needs are met by the ability to sort by coffee dosage

## Features

### Existing Features

- Feature 1: User can view brews and apply filters and sorting. Clicking on a brew reveals additional information, including brewer position, brew time, water temperature and process
- Feature 2: User can contribute a brew. Range sliders and dropdown boxes were employed for input validation purposes, which is essential for effective filtering and sorting
- Feature 3: User can edit an existing brew
- Feature 4: User can delete an existing brew. On click of delete button, a modal is presented to ask for confirmation
- Feature 5: User can 'like' a brew, which increments the likes count by 1

### Features Left to Implement

- Potential Feature 1: Graphs analysing traits of winning brews
- Potential Feature 2: Ability to sort table by clicking column header - clicking on current sort field changes toggles direction
- Potential Feature 3: Ability to share brew with a friend via a link
- Potential Feature 4: User login functionality so that users can 'star' brews to keep a list of favourites. Also, users would only be able to edit/delete their own brews.

## Database

The document-based NoSQL database, MongoDB was employed. PyMongo is used to interact with the database.

The database has a single collection named 'brews', with the following fields:

| Field         | Type     | Description                                |
| :------------ | :------- | :----------------------------------------- |
| \_id          | ObjectId | ID is auto-created by MongoDB              |
| barista       | String   | Name of barista or user                    |
| brew_name     | String   | Name of brew                               |
| brew_source   | String   | Source of brew (WAC or Average Joe)        |
| brewer        | String   | Brewing method (Upright or Inverted)       |
| coffee_dose_g | Double   | Coffee dose (grams)                        |
| country       | String   | Barista's country of origin (optional)     |
| filter        | String   | Filter type (eg. Paper, Metal)             |
| grind         | Int32    | Grind size from 1-10 (1: Fine, 10: Coarse) |
| likes         | Int32    | Number of Likes (initial value: 0)         |
| steps         | Array    | Process - each element in array is a step  |
| place         | String   | Podium place if Champ brew                 |
| water_temp_c  | Int32    | Water temperature (Celsius)                |
| year          | String   | Year - set to current year when brew added |

## Technologies Used

- [Autoprefixer CSS Online](https://autoprefixer.github.io/) : used to add vendor prefixes.
- [Balsamiq](https://balsamiq.com/) : used to create wireframes.
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) : used extensively to ensure device responsiveness.
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) : styling language.
- [Favicon Generator](https://www.favicon-generator.org) : used to create a 16x16 icon, displayed next to page title in browser.
- [Git](https://git-scm.com/) : used for version control.
- [GitHub](https://github.com) : used to host code repository and to deploy project (via GitHub Pages).
- [Google Fonts](https://fonts.google.com/) : used for the main font - 'Share Tech'.
- [HTML5](https://www.w3.org/html) : used for page structure.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) :
- [jQuery](https://jquery.com/) : used to select and manipulate HTML elements.
- [Material Icons](https://material.io/) : used for icons and fonts.
- [Materialize CSS](https://www.materializecss.com/) : used as responsive front-end framework.
- [mongoDB](https://www.mongodb.com/) : used as database.
- [VSCode](https://code.visualstudio.com) : preferred code editor.
- [W3C Validator](https://jigsaw.w3.org) : used to validate HTML & CSS.

## Testing

Extensive manual testing was conducted to ensure the site functions and looks well on all major browsers (Chrome, Firefox, Safari, Edge) and device sizes.

### Desktop Testing

Brew Browser Page

- Filters: each checkbox selection/deselection causes expected filtering in table
- Sorting: each sort field sorts correctly, with expected sort direction
- Reset filters button refreshes page with all checkboxes filled.
- Likes: clicking the like button increases like count by 1
- Pagination display: correct record range for displayed records. (eg 'showing 1-8')
- Pagination buttons: correct number of pages are displayed based on filtered records returned.
- Pagination buttons: left chevron is disabled and unclickable when on first page
- Pagination buttons: right chevron is disabled and unclickable when on last page
- Links: no broken links. External links open in new window (ie target="\_blank")
- Feedback: all interactive elements (ie checkboxes, buttons, like button, navigation menu links) change appearance on hover
- Tooltips: appear on hover of medal icons
- 'Collapsible' materialize component: on click of a record, additional information is revealed and is correct.
- Edit button: takes user to Edit Page of selected record
- Delete button: triggers modal, asking for delete confirmation. Confirm delete button deletes record from database.
- Confirm delete button: on click a confirmation 'Toast' message is displayed: 'Deleted'
- Colours: all text is readable with good colour contrast
- Background Image: sticks to bottom of body during scroll
- Forward and Back browser buttons are never required, but if clicked, don't break the site.

Add Brew page

- Form: required fields (Brew Name, Barista Name) have validation (red: invalid, green: valid)
- Form: country field shows suggestion list of countries
- Form sliders: adjusting range sliders updates the displayed value to the right of each slider
- Form process field: on carriage return keypress cursor moves to next line of text area (instead of submitting the form)
- Submit form button posts all fields correctly to the database
- On click of submit button, a confirmation 'Toast' message is displayed: 'Added'
- Cancel form button returns to Brew Browser page
- Navigation buttons function
- Forward and Back browser buttons are never required, but if clicked, don't break the site.

Edit Brew page

- All form fields (input boxes, dropdowns, sliders, text areas) are prefilled with existing data from database.
- Update button submits form and record is updated correctly in database
- On click of update button, a confirmation 'Toast' message is displayed: 'Updated'
- Cancel button returns to Brew Browser
- Navigation buttons function
- Forward and Back browser buttons are never required, but if clicked, don't break the site.

About page

- Embedded video plays
- Navigation buttons function
- Forward and Back browser buttons are never required, but if clicked, don't break the site.

404 Error Page

- When an incorrect URL is entered, 404 Page is displayed with image
- Return home button takes user back to Brew Browser page
- Navigation buttons function

### Mobile and Tablet Tests

The above Desktop Tests were also conducted on mobile and tablet devices (via Chrome DevTools). In addition, the following mobile and tablet-specific tests were run:

Brew Browser Page (Mobile)

- Navigation links collapse into 'burger' icon
- Burger icon expands side navigation bar, with all links functioning

The following tests failed:

| Issue No. | Test Name                                       | Issue                                                                        | Resolved? | Action Taken                                                             |
| :-------- | :---------------------------------------------- | :--------------------------------------------------------------------------- | :-------- | :----------------------------------------------------------------------- |
| 1         | Content is not squeezed or overlapping (Mobile) | Brew Browser table has overlapping horizontal content, even with small text. | Yes       | Added materialise class 'hide-on-med-and-down' to bean and grinder icons |
| 2         | Text is appropriately sized (Mobile)            | Title text in navigation bar is too large, causing text to overflow          | Yes       | Title text added to mobile media query                                   |
| 3         | Form entry is effective and intuitive (Mobile)  | Range slider displays do not update their values on change (Mobile)          | Yes       | Range slider event listener changed from 'onclick' to 'onchange'         |

### Code Validation

| Code                                                            | Result |
| :-------------------------------------------------------------- | :----- |
| CSS ([W3C](https://jigsaw.w3.org/css-validator/))               | PASS   |
| HTML ([W3C](https://validator.w3.org/))                         | PASS^  |
| Javascript with no major errors ([jshint](https://jshint.com/)) | PASS   |
| Python ([jshint](https://pep8online.com/))                      | PASS^^ |

^ The following classes of errors were deemed not applicable, as the validator did not take into account Flask and Jinja templating:

- 'Error: Bad value {{url_for('index')}} for attribute href on element a: Illegal character in path segment: { is not allowed.'
- 'Error: Start tag seen without seeing a doctype first. Expected \<!DOCTYPE html>.'
- 'Text not allowed in element ul in this context' - {% for brew in brews %}
- 'Element head is missing a required instance of child element title.'

^^ 1 line flagged E501 'line too long' by several characters

## Deployment

### Heroku

The application was deployed to Heroku, via the following steps:

1. Heroku.com > Create new app > App name: aeropress-hub, Region: Europe
2. Deploy > Deployment method > Link GitHub account
3. Select repository 'milestone-3'
4. Select branch: 'master'
5. Set Config Vars: Heroku Settings > Config Vars:
   - IP: 0.0.0.0
   - PORT: 5000
   - MONGO_URI: mongodb+srv://[user]:[password]@myfirstcluster-bgxgx.mongodb.net/aeropress?retryWrites=true&w=majority
6. Manual Deploy > Deploy Branch (master)
7. Heroku Website > Open App

### Local Deployment

1. 'Clone or download' repository from https://github.com/tdunn891/milestone-3, or from command line:

   `git clone https://github.com/tdunn891/milestone-3`

2. If your IDE doesn't include a virtual environment, create one (see Python docs: [Creation of virtual environments](https://docs.python.org/3/library/venv.html):

   `python3 venv /path/to/new/virtual/environment`

3. Activate virtual environment:

   `source /path/to/new/virtual/environment`

4. Install dependencies in requirements.txt via 'pip':

   `pip -r requirements.txt`

5. Run app:

   `python3 app.py`

6. Go to Local Host in browser to view:

   `http://127.0.0.1:5500/`

## Credits

### Content

- World AeroPress Champs logo and About page text source: [World AeroPress Championships](https://aero.press/)
- Championship Recipes web-scraped from [AeroPress.com](https://aeropress.com/championships/wac-recipes/)

### Media

Images sourced from [Shutterstock](https://www.shutterstock.com/) (Standard License)

- [Beans Background Image](https://www.shutterstock.com/image-photo/coffee-beans-isolated-on-white-background-385820884?src=library)
- [AeroPress at Lake Bled](https://www.shutterstock.com/image-photo/mug-mockup-aeropress-next-sitting-traveler-1587478897?src=library)
- [Four Hands](https://www.shutterstock.com/image-photo/empty-clear-aeropress-filter-cap-two-496228861?src=library)
- [Barista](https://www.shutterstock.com/image-photo/professional-barista-preparing-coffee-alternative-method-515650723?src=library)

Embedded [video](https://www.youtube.com/embed/u928bWvxrZ8) from World AeroPress Championships YouTube Channel

Icons sourced from: [FlatIcon](https://www.flaticon.com/)

- Brand Icon by [Skyclick](https://www.flaticon.com/authors/skyclick)
- Coffee Beans Icon by [smalllikeart](https://www.flaticon.com/authors/smalllikeart)
- Grinder Icon by [catkuro](https://www.flaticon.com/authors/catkuro)
- Thermometer Icon by [Freepik](https://www.flaticon.com/authors/freepik)
- AeroPress Icon by [dDara](https://www.flaticon.com/authors/ddara)

### Acknowledgements

[Pagination Tutorial (YouTube)](https://www.youtube.com/watch?v=Lnt6JqtzM7I)

Big thanks to friends and family for help with testing and feedback.
