# SOAR Automation Tests

This repository contains automated tests for web and mobile applications, showcasing skills in test automation using Python.

## Technologies Used
- **Python**: Core programming language.
- **Selenium**: Browser automation framework.
- **Pytest**: Testing framework for writing and running tests.
- **WebDriver Manager**: Simplifies management of WebDriver binaries.
- **Appium**: Mobile automation framework for Android and iOS apps.

## Project Overview
The `soar` project is organized into two main sections:
- **`Web_App_Tests`**: Automated tests for web applications, with each task in its own subfolder:
- `Task_1`: Tests navigation, scrolling, dropdown selection, and item display on the Juice Shop website (`https://juice-shop.herokuapp.com/#/`). 
- `Task_2`: Tests clicking the "Apple Juice" product, asserting a popup with an image appears, expanding the review if present, and closing the form.
- **`Mob_App_Tests`**: Automated tests for mobile applications (using the Wikipedia Alpha app, `org.wikipedia.alpha.apk`), with each task in its own subfolder:
- `Task_1`: Tests launching the app, scrolling down to the end, navigating to "My Lists," "History," and "Nearby" pages (waiting 3 seconds each), returning to home via "Browse," and scrolling up to the first topic.
- `Task_2`: Tests interacting with the search bar, entering "New York," asserting search results appear, and returning to the home page.

## Project Structure 
soar/
├── Web_App_Tests/
│   ├── Task_1/
│   │   └── test_task1.py  # Web test for Task 1
│   ├── Task_2/
│   │   └── test_task2.py  # Web test for Task 2
│   ├── Task_3/
│   │   └── test_task3.py  # Web test for Task 3
│   ├── Task_4/
│   │   └── test_task4.py  # Web test for Task 4
├── Mob_App_Tests/
│   ├── Task_1/
│   │   └── test_task1.py  # Placeholder for mobile test
│   └── ...
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

## Setup Instructions
1. **Prerequisites**: Ensure Python 3.x is installed on your system.
2. **Clone the Repository**: Download the project to your local machine.
