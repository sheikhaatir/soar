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
- `Task_3`: Tests opening the overflow menu, navigating to the settings page, switching off all toggles, and returning to the main screen.

## Setup Instructions
Follow these steps to set up and run the tests on your local machine. Instructions are separated for Web Automation and Mobile Automation to ensure clarity and ease of replication.

### Web Automation Setup
1. **Prerequisites**:
   - Ensure Python 3.x is installed (check with `python --version`).

2. **Clone the Repository**:

git clone https://github.com/sheikhaatir/soar.git

Navigate to the root directory: 
cd soar

3. **Set Up Python Virtual Environment**:
- Create a virtual environment to isolate dependencies:
python -m venv .venv
- Activate it:
- On Windows: ..venv\Scripts\activate
- On Linux/Mac: source .venv/bin/activate
- Confirm activation (you should see `(.venv)` in the terminal prompt).

4. **Install Web Testing Dependencies**:
- Install required packages for web tests using the `requirements.txt` file:
pip install -r requirements.txt
- Verify installation (e.g., `pip show selenium`, `pip show pytest`, `pip show webdriver-manager`).

5. **Run Web Tests**:
- **Run All Web Tests**: From the `soar/` root directory:
pytest Web_App_Tests/Task_1/test_task1.py

### Mobile Automation Setup
1. **Prerequisites**:
- Ensure Python 3.x, Node.js, npm, Java Development Kit (JDK) 8 or higher, and Android Studio or SDK are installed.
- Check versions:
- Python: `python --version`
- Node.js/npm: `node -v` and `npm -v`
- Java: `java -version`
- Android SDK: Ensure `ANDROID_HOME` is set (e.g., `echo %ANDROID_HOME%` on Windows) and `adb` is available (`adb devices`).

2. **Clone the Repository**: 
`git clone https://github.com/sheikhaatir/soar.git` (Ignore this step if already cloned the repo)
Navigate to the root directory:
cd soar

3. **Set Up Python Virtual Environment**: (Ignore this step if already created a venv)
- Create a virtual environment to isolate dependencies: 
python -m venv .venv
- Activate it:
- On Windows: ..venv\Scripts\activate
- On Linux/Mac: source .venv/bin/activate
- Confirm activation (you should see `(.venv)` in the terminal prompt).

4. **Install Mobile Testing Dependencies**:
- Install required packages for mobile tests using the `requirements.txt` file:
pip install -r requirements.txt
- Verify installation (e.g., `pip show Appium-Python-Client`, `pip show pytest`).

5. **Install Appium Server**:
- Install Appium globally (not in the repo) using npm:
npm install -g appium@latest
- Install `appium-doctor` for diagnostics:
npm install -g appium-doctor
- Run `appium-doctor` to verify your environment:
appium-doctor
- Fix any issues reported (install JDK, set environment variables and PATH `ANDROID_HOME`, `ANDROID_SDK_ROOT`, `JAVA_HOME`).

6. **Set Up Android Emulator/Device**:
- Install Android Studio and set up an emulator, or use a physical device with USB debugging enabled.
- Run `adb devices` to list connected devices/emulators (e.g., `id` for your device).
- Place the provided `.apk` file (`org.wikipedia.alpha.apk`) in the `app/` directory (e.g., `soar/app/org.wikipedia.alpha.apk`).
- Ensure the `deviceName` in your test scripts matches your device/emulator ID .

7. **Start Appium Server**:
- Open a separate terminal (outside the Python environment) and start the Appium server: 
appium
- Verify it listens on `http://127.0.0.1:4723` (check logs for errors).

8. **Run Mobile Tests**:
- **Run All Mobile Tests**: From the `soar/` root directory:
pytest Mob_App_Tests/

## Testing Approach
- **Web Automation Tests**: Use Selenium with Pytest to automate the Juice Shop website, handling dynamic content, scrolling, dropdowns, and product interactions with robust error handling, waits, and precise selectors.
- **Mobile Automation Tests**: Use Appium with Pytest to automate the Wikipedia Alpha app, performing gestures (e.g., swipes), navigating menus, searching, and asserting UI elements with precise AppiumBy selectors, error handling, and waits.

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


