Workout Tracker with Nutritionix API and Google Sheets Integration
This Python script allows users to track their workouts and automatically log the details into a Google Sheet. The workout details are retrieved using the Nutritionix API, providing accurate data on exercises performed, including duration and calories burned.

Features:
Nutritionix API Integration: Utilizes the Nutritionix API to fetch exercise details based on user input, such as exercise name, gender, weight, height, and age.

Google Sheets Integration: Logs the workout details, including date, time, exercise name, duration, and calories burned, into a Google Sheet for easy tracking and analysis.

How to Use:
Set Up Environment Variables:

Obtain API credentials from Nutritionix and set them as environment variables (APP_ID, API_KEY).
Set your Nutritionix account credentials (USERNAME, PASSWORD) and other necessary endpoints as environment variables.
Run the Script:

Input the exercises you performed when prompted.
The script fetches exercise details from Nutritionix API and logs them into a Google Sheet.
Google Sheets Authentication:

Basic Authentication is implemented using your Google Sheets username and password.
Dependencies:
requests: For making HTTP requests to the Nutritionix API and Google Sheets.
datetime: For obtaining current date and time.
os: For handling environment variables.
Note:
Ensure that your Google Sheets API credentials are set up correctly and that the necessary libraries are installed.

Feel free to contribute, report issues, or suggest improvements! Happy exercising! 🏋️‍♂️💪
