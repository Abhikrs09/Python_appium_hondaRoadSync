## ⚙️ Setup Instructions

### Clone the project

```sh
  git clone https://github.com/Abhikrs09/Python_appium_hondaRoadSync.git
  cd automation-test-python
```

### Create and activate a virtual environment

```sh
  python -m venv .venv
  .venv/scripts/activate
```

### Install Project Dependencies

```sh
  pip install -r requirements.txt
```

## Setup Tools
Before running tests, it is necessary to set up different tools.

### Mobile App
- Download the test mobile app from [here](https://play.google.com/store/apps/details?id=com.honda.ms.dm.sab&hl=en).
- Move the downloaded APK file inside the `src/` directory and rename it to `honda_roadsync.apk`.

### Appium Installation
- Install Node.js and npm (version >=8, LTS recommended) from [Node.js](https://nodejs.org/en) and [npm](https://www.npmjs.com/).
- Install Appium globally:
  ```sh
  npm install -g appium
  ```
- Install the UiAutomator2 driver:
  ```sh
  appium driver install uiautomator2
  ```
- Validate the setup:
  ```sh
  appium driver install doctor
  appium driver doctor uiautomator2
  ```

### Android SDK Setup
- Download and install [Android Studio](https://developer.android.com/studio).
- Set up the `ANDROID_HOME` environment variable to point to the Android SDK installation directory.
- Add the `platform-tools` directory to your system's PATH.
- Common ADB commands:
  ```sh
  adb devices  # List connected devices
  adb install <path-to-apk>  # Install an APK
  adb shell  # Access device shell
  ```

### Java JDK Setup
- Install [Java JDK](https://jdk.java.net/) and set up the `JAVA_HOME` environment variable.

### Appium Inspector
- Download [Appium Inspector](https://github.com/appium/appium-inspector/releases) to inspect mobile app elements.

## 🔔 Slack Integration
- Generate a Slack Webhook URL from [Slack Webhooks](https://api.slack.com/messaging/webhooks).
- Store the webhook in a `.env` file:
  ```sh
  SLACK_WEBHOOK_URL=<your-webhook-url>
  ```

## 🏃‍♂️ Running Tests

### Run Test Cases
- Start an Android emulator.
- Start the Appium server in a separate terminal.
- Run tests:
  ```sh
  pytest -x -v
  ```

### Run Tests with Logs
- To run tests with log output:
  ```sh
  pytest --log-cli-level=INFO
  ```
  OR
  ```sh
  pytest -s --capture=no
  ```

### Generate Allure Report
- Run tests with Allure reporting:
  ```sh
  pytest --alluredir=reportallure
  allure serve reportallure
  