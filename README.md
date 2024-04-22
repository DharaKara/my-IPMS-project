# InsureWheels Web Application Documentation

## Overview
InsureWheels is an insurance policy management system designed to simplify the process of comparing car insurance quotes. As a Comparative Services authorized financial service provider, InsureWheels offers comprehensive, third party, and third party, fire, and theft insurance options.

## Key Features

1. **User Authentication**: Easily register and log in to access the full functionality of the application. Passwords are securely hashed for user security.
2. **Intuitive Navigation**: User-friendly navigation bar for effortless access to various pages including Home, Login, Register, Contact Us, FAQs, Partners, and Partner Details.
3. **Quote Comparison**: Users can compare insurance quotes from different partners to make informed decisions. Quotes are displayed in a visually appealing card format with detailed information.
4. **Vehicle Management**: Add, edit, or delete vehicles to tailor insurance quotes to your needs. Users can input vehicle details including make, model, year, and additional features.
5. **Driver Details**: Input driver information for accurate insurance quotes. Users can provide driver details such as license type, issue date, and car insurance history.
6. **Partner Integration**: Quotes from various insurance partners are displayed, providing users with multiple options to choose from. Each partner's logo and key information are showcased for easy comparison.
7. **Confirmation**: Receive confirmation upon selecting a quote, ensuring the quotation process is complete. Users are notified that their quote request has been successfully sent to the selected partner for further processing.
8. **FAQs Page**: Find answers to commonly asked questions about the application and its features. FAQs are organized into categories for easy navigation.
9. **Contact Us Page**: Reach out to the support team for assistance or inquiries. A contact form is provided for users to submit their queries.
10. **Partners Page**: Explore detailed information about insurance partners and their offerings. Partners are listed with their logos, names, and brief descriptions, with the option to view more details.

## How to Use

1. **Homepage**: Explore navigation links and learn about the types of insurance offered. Testimonials provide feedback from satisfied users.
2. **Login/Register**: Register for an account or log in if you already have one. Password recovery options are available for forgotten passwords.
3. **Profile Editing**: Edit your profile information for accuracy. Users can update their personal details, including name, email, and contact information.
4. **Add Car**: Add your vehicles using the provided form. Input vehicle details accurately to receive precise insurance quotes.
5. **Car Summary**: View a summary of your vehicles and manage them as needed. Edit or delete vehicles to keep your profile up to date.
6. **Add Driver**: Input driver details to refine insurance quotes. Provide accurate information to ensure quotes reflect your specific circumstances.
7. **Get Quote**: Click "Get Quote" to initiate the quotation process. Review the quotes from different partners and select the most suitable option.
8. **Quote Comparison**: Compare quotes from different insurance partners to find the best option. Consider factors such as premiums, excess amounts, and additional benefits.
9. **Quote Selection**: Select a quote and receive confirmation that it has been sent to the partner for processing. Await further communication from the selected partner regarding your insurance policy.

## Technology Stack

- **Backend**: Developed with Python using the Flask framework. Secure user authentication and data storage are implemented.
- **Frontend**: HTML/CSS/Bootstrap for user interface and styling. Responsive design ensures compatibility across devices.
- **Dynamic Content**: Jinja Templates for generating dynamic HTML content. Content is rendered dynamically based on user interactions.
- **Data Management**: Database models organized in a models folder. SQLAlchemy ORM used for database operations and management.
- **Routes Structure**: Organized routes with blueprints for improved code organization. Separation of concerns ensures modular and maintainable code.
- **Inheritance and Styling**: Inheritance is utilized with a base HTML template (`base.html`) to maintain consistency across pages. A static CSS file (`style.css`) is used to apply consistent styling and improve user experience.

## Conclusion

InsureWheels simplifies car insurance policy management with its user-friendly interface and comprehensive features. Whether you're comparing quotes or managing your policy details, InsureWheels ensures a smooth and hassle-free experience.

## Some easy to access command lines
activate my env
.\myenv\Scripts\Activate.ps1

enter run on dev mode
flask --app app run --debug

freeze installed packages to requirements.txt
pip freeze > requirements.txt
pip install -r requirements.txt

