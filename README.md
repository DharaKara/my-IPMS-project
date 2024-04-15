# InsureWheels Web Application Documentation

## Overview
InsureWheels is an insurance policy management system designed to streamline the process of comparing car insurance quotes. InsureWheels is a Comparative Services authorized financial service provider, offering three types of car insurance: comprehensive, third party, and third party, fire, and theft.

## Features

1. **User Authentication**: Users can register and log in to access the full functionality of the application.

2. **Navigation**: The web application features a user-friendly navigation bar allowing easy access to various pages.

3. **Quote Comparison**: Registered users can add their cars and drivers to get insurance quotes from different partners, facilitating easy comparison of premiums and excess amounts.

4. **Add/Edit/Delete Cars**: Users can manage their vehicles by adding, editing, or deleting them from their profile.

5. **Add Driver Details**: Users can input driver information to generate accurate insurance quotes.

6. **Partner Integration**: Quotes from various insurance partners such as MiWay, Santam, Old Mutual, and First for Women are displayed in card format, providing users with multiple options to choose from.

7. **Feedback and Confirmation**: Upon selecting a quote, users receive confirmation that their quotation process is complete, and the quote has been sent to the selected partner for further processing.

## Usage

1. **Homepage**: The landing page displays navigation links, including login, register, contact us, FAQs, partners, and partner details. Users can also view the types of insurance offered and read testimonials.

2. **Login/Register**: Users can register for an account or log in if they already have one.

3. **Profile Editing**: Once logged in, users can edit their profile information.

4. **Add Car**: Registered users can add their vehicles by filling out an add car form.

5. **Car Summary**: After adding cars, users can view a summary of their vehicles and edit or delete them as needed.

6. **Add Driver**: Users can input driver details to generate accurate insurance quotes.

7. **Get Quote**: Upon completing the necessary information, users can click "Get Quote" to initiate the quotation process.

8. **Quote Comparison**: The application displays quotes from different insurance partners, allowing users to compare premiums and excess amounts.

9. **Quote Selection**: Users can select a quote they are interested in, which triggers a confirmation message indicating that the quote has been successfully sent to the partner for further processing.

## Technology Stack

- **Python**: Backend development using the Flask framework.
- **HTML/CSS/Bootstrap**: Frontend development for user interface and styling.
- **Jinja Templates**: Templating engine for generating dynamic HTML content.
- **Database Models**: Models folder contains all database models for data management.
- **Routes Organization**: Routes are organized in a routes folder with blueprints for improved code structure and maintainability.

## Conclusion

InsureWheels provides a user-friendly platform for managing car insurance policies, allowing users to easily compare quotes from various insurance partners. With its intuitive interface and comprehensive features, InsureWheels simplifies the insurance quotation process, ensuring a smooth user experience.

## Some easy to access command lines
activate my env
.\myenv\Scripts\Activate.ps1

enter run on dev mode
flask --app app run --debug

freeze installed packages to requirements.txt
pip freeze > requirements.txt
pip install -r requirements.txt

