# Blood Donation Management System

A simple web application that allows users to submit their blood donation details such as Name, Department, Blood Group, Contact, Email, USN, Year and age information. The system stores the data in a MySQL database, helping organizations manage blood donations efficiently.

## Features

- **User-friendly form** for submitting blood donation details.
- **Database storage**: Donor details are saved in a MySQL database (`blood_group`).
- **Real-time validation**: Ensures data integrity during form submission.
- **Responsive design**: Works well on all devices.
- **Error handling**: Displays appropriate error messages for failed submissions (e.g., duplicate USN).

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- MySQL server
- pip (Python package installer)

## How it Works

1. **Database Creation**: At the beginning, a MySQL database named `blood_group` is created, and the necessary table `donors` is set up with the following columns:
   - `Name`
   - `Department`
   - `USN`
   - `Year`
   - `BloodGroup`
   - `Contact`
   - `Email`
   - `Age`

2. **User Fills in the Form**: The user enters their blood donation details (name, department, USN, year, blood group, contact, email, age) on the web form.

3. **Form Submission**: When the user clicks "Submit," the form data is sent via a POST request to the `/submit` endpoint.

4. **Data Processing**: The Flask app processes the submitted data:
   - It retrieves the form values from the request.
   - Validates the data (e.g., checks for duplicate USN).

5. **Database Storage**: The app connects to the MySQL database and stores the form data in the `donors` table.

6. **Confirmation**: After successful data insertion, a confirmation message is returned and displayed to the user, thanking them for their blood donation.
