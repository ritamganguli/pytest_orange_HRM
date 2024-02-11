# Pytest OrangeHRM Project

This repository contains automated tests for the OrangeHRM web application, leveraging the power and flexibility of pytest. The tests encompass a wide range of functionalities within the application, aiming to ensure both its reliability and performance.

## Features

- **Admin Panel Testing**: Validates the processes of creating, editing, and deleting users, as well as managing user roles.
- **Dashboard Testing**: Ensures the dashboard displays all necessary components correctly and functions as expected for different user roles.
- **Buzz Page Testing**: Assesses the functionality of the Buzz page, including the ability to post updates, comment, and like posts.

## Installation

To run these tests, ensure that Python is installed on your system, along with pytest and other required packages.

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ritamganguli/pytest_orange_HRM.git
    ```
    
2. **Install the required dependencies:**
    ```bash
    cd pytest_orange_hrm
    pip install -r requirements.txt
    ```

## Running Tests

To execute all tests, run the following command in the root directory of the project:
```bash
py.test -v -s
```

To run the test on a specific browser lets say chrome:
```bash
py.test --browser Chrome -v -s
```

