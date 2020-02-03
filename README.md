# AeroPress Brews - Milestone 3: Data-Centric Development

## Contents

1. [**Project Purpose**](#project-purpose)

2. [**UX**](#ux)

   - [**Strategy**](#strategy)
   - [**Scope**](#scope)
   - [**Structure**](#structure)
   - [**Skeleton**](#skeleton)
     - [**Wireframes**](#wireframes)
   - [**Surface**](#surface)
   - [**User Stories**](#user-stories)

3. [**Features**](#features)

   - [**Existing Features**](#existing-features)
   - [**Features Left to Implement**](#features-left-to-implement)

4. [**Database**](#Database)

5. [**Technologies Used**](#technologies-used)

6. [**Testing**](#testing)

   - [**Manual Testing**](#manual-testing)

7. [**Deployment**](#deployment)

8. [**Credits**](#credits)

   - [**Contents**](#contents)
   - [**Media**](#media)
   - [**Acknowledgements**](#acknowledgements)

## Project Purpose

AeroPress Hub was developed to centralise and showcase AeroPress coffee brews, from both champion baristas and AeroPress enthusiasts. Users can add their own, edit or delete existing brews. This application aims to provide value to the niche, passionate global community that exists around this humble coffee brewing device.

## UX

### Strategy

Site Objectives:

- Provide a hub for AeroPress recipes

User Needs:

- Contribute, view, edit, and delete brews

The following Opportunities/Problems table was used to determine which strategic priorities the UX efforts should address (in this order):

| Opportunity/Problem                                  | Importance | Viability/Feasibility |
| ---------------------------------------------------- | :--------: | :-------------------: |
| A. Centralise AeroPress recipes                      |     5      |           5           |
| B. Allow contributions, edits, and deletion of brews |     5      |           5           |
| C. Encourage AeroPress purchases via affiliate links |     2      |           2           |

### Scope

#### Functional Specifications

In considering functional specifications,

Feature Set:

- Filterable, sortable table of communal dataset of brews from World AeroPress Champions and regular user brews.
- Ability to add brew to communal data set

#### Content Requirements

In order to provide the value of the above features, the following content is required:

- Material collapsible collection
- Checkboxes for filtering
- Select Dropdowns for sorting and for form input

### Structure

#### Interaction Design

Consistency & Predictability

Feedback:

Tooltips are used to offer additional information, eg Grind Size.

#### Information Architecture

### Skeleton

#### Wireframes

Two sets of wireframes were created in the early development stage to help set out the content and layout in differing device sizes.

<!-- TODO: insert wireframe links -->

### Surface

Colours: Coffee Brown was chosen as the primary colour for obvious reasons.

Fonts: A playful font was selected to emulate the fun nature of the World AeroPress Championships.

### User Stories

User stories:

- User 1 - "As a user who has just bought an AeroPress but doesn't know how to use it, I want to see how the champion baristas use it."
- User 2 - "As a user who has discovered an innovative new way to brew with the AeroPress, I want to share it with the community."
- User 3 - "As a user who is interested in analysing what makes a gold medal brew, I want to be able to hone in (filter) on these brews."
- User 4 - "As a user who has just purchased a metal filter, I want to see how other uses are brewing with it."
- User 5 - "As a user who has tried a recipe submitted by another user, I want to be able to edit (improve) it for the benefit of other users."
- User 6 - "As a user who loves high coffee dosages, I want to sort the dataset by dosage."

How their needs are met:

- User 1's needs are met by having the ability to browse through champion brews with detailed steps.
- User 2's needs are met by the ability to share a brew via the Add Brew page.
- User 3's needs are met by the ability to filter by Place: Winners First
- User 4's needs are met by the ability to filter by metal filter
- User 5's needs are met by the ability to Edit a brew
- User 6's needs are met by the ability to sort by coffee dosage

## Features

### Existing Features

- Feature 1: User can view brews and apply filters and sorting
- Feature 2: User can contribute a brew with details and process
- Feature 3: User can delete a brew
- Feature 4: User can edit an existing brew
- Feature 5: User can 'like' a brew, which increments the like count in the database by 1

### Features Left to Implement

Potential Feature 1: Graphs analysing traits of winning brews
Potential Feature 2: Ability to sort table by clicking header - clicking on current sort field changes toggles direction
Potential Feature 3: Ability to share brew with a friend via a link

## Database

The document-based NoSQL database, MongoDB was employed. PyMongo interacts with the database.

Schema

| Field         | Type     | Description                                                 |
| :------------ | :------- | :---------------------------------------------------------- |
| \_id          | ObjectId | ID is auto-created by MongoDB                               |
| brew_name     | String   | Name of brew                                                |
| year          | String   | Year                                                        |
| place         | String   | Podium place if Champ brew. If Average Joe brew, set to 100 |
| barista       | String   | Name of barista or user                                     |
| country       | String   | Country of origin                                           |
| brew_source   | String   | Source of brew, either WAC or Average Joe (regular user)    |
| steps         | Array    | Process. Each element in array is a step                    |
| coffee_dose_g | Double   | Coffee dose (grams)                                         |
| grind         | Int32    | Coffee grind out of 10 (1: Fine, 10: Coarse)                |
| water_temp_c  | Int32    | Water temperature (Celsius)                                 |
| brewer        | String   | Brewing method (either Upright or Inverted)                 |
| filter        | String   | Filter type                                                 |
| likes         | Int32    | Number of Likes                                             |

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
- [Materialize CSS](https://www.materializecss.com/) : used as reponsive front-end framework.
- [mongoDB](https://www.mongodb.com/) : used as database.
- [VSCode](https://code.visualstudio.com) : preferred code editor.
- [W3C Validator](https://jigsaw.w3.org) : used to validate HTML & CSS.

## Testing

### Manual Tests

Desktop Tests

Brew Browser Page

- Filters: each checkbox selection/unselection causes expected filtering in table
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
- Delete button: triggers modal, asking for delete confirmation. Confim delete button deletes record from database.
- Confirm delete button: on click a confirmation 'Toast' message is displayed: 'Deleted'
- Colours: all text is readable with good colour contrast
- Background Image: sticks to bottom of body during scroll

Add Brew page

- Form: required fields (Brew Name, Barista Name) have validation (red: invalid, green: valid)
- Form: country field shows suggestion list of countries
- Form sliders: adjusting range sliders updates the displayed value to the right of each slider
- Form process field: on carriage return keypress cursor moves to next line of text area (instead of submitting the form)
- Submit form button posts all fields correctly to the database
- On click of submit button, a confirmation 'Toast' message is displayed: 'Added'
- Cancel form button returns to Brew Browser page
- Navigation buttons function

Edit Brew page

- All form fields (input boxes, dropdowns, sliders, text areas) are prefilled with existing data from database.
- Update button submits form and record is updated correctly in database
- On click of update button, a confirmation 'Toast' message is displayed: 'Updated'
- Cancel button returns to Brew Browser

About page

- Embedded video plays
- Navigation buttons function

404 Error Page

- When an incorrect url is entered, 404 Page is displayed with image
- Return home button takes user back to Brew Browser page
- Navigation buttons function

Mobile and Tablet Tests

The above Desktop Tests were performed on a mobile device. The following mobile and tablet-specific tests were conducted:

Brew Browser Page

- No content is squished or overlapping
- Navigation links collapse into 'burger' icon
- Burger icon expands side navigation bar, with all links functioning

Extensive manual testing was conducted to ensure the site functions and looks well on all major browsers (Chrome, Firefox, Safari, Edge) and device sizes.

The following tests failed:

| Issue No. | Test Name   | Issue       | Resolved?   | Action Taken |
| :-------- | :---------- | :---------- | :---------- | :----------- |
| 1         | placeholder | placeholder | placeholder | placeholder  |

Code Validation

| Code                                                            | Result |
| :-------------------------------------------------------------- | :----- |
| CSS ([W3C](https://jigsaw.w3.org/css-validator/))               | PASS   |
| HTML ([W3C](https://validator.w3.org/))                         | PASS^  |
| Javascript with no major errors ([jshint](https://jshint.com/)) | PASS   |

^ The following classes of errors were deemed not applicable, as the validator did not take into account Flask and Jinja templating:

- 'Error: Bad value {{url_for('index')}} for attribute href on element a: Illegal character in path segment: { is not allowed.'
- 'Error: Start tag seen without seeing a doctype first. Expected \<!DOCTYPE html>.'
- 'Text not allowed in element ul in this context' - {% for brew in brews %}
- 'Element head is missing a required instance of child element title.'

## Deployment

The application was deployed to Heroku, using the following steps:

## Credits

### Content

- WAC Logo from [World AeroPress Championships](https://aero.press/)
- Championship Recipes sourced from [AeroPress.com](https://aeropress.com/championships/wac-recipes/)
- Coffee icons: [FlatIcon](https://www.flaticon.com/)
  <!-- TODO: list icon creators (most in Notion) -->

### Media

- Images from [Shutterstock](https://www.shutterstock.com/) (Standard License)

### Acknowledgements

Pagination: https://www.youtube.com/watch?v=Lnt6JqtzM7I
