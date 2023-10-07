# Thank-U-Next - Automated Club Moderation Tool

## Introduction

Thank-U-Next is an automated tool designed for Juni Club Moderators. It simplifies the process of managing multiple club accounts by automating the login and logout procedures, making club moderation more efficient.

## Prerequisites

Before using Thank-U-Next, ensure you have the following prerequisites:

1. **Python**: Ensure you have Python installed on your computer. If not, download it from the [official Python website](https://www.python.org/downloads/).

2. **Required Python Packages**: Install the required Python packages by running this command in your terminal or command prompt:

   ```bash
   pip install selenium webdriver_manager

1. Club Account Information: Create a text file named accounts.txt with the account information you intend to use for club moderation. Use the following format:

   ```bash
   username1
   password1
   username2
   password2

Usage
To use Thank-U-Next, follow these steps:

**1. Clone or Download the Repository:** Clone this repository or download it as a ZIP file and extract it to your preferred location.

**2. Navigate to the Project Directory:** Open your terminal or command prompt and navigate to the directory where you've saved the Thank-U-Next program.

**3. Run the Program:** Execute Thank-U-Next by running the following command:

   ```bash
   python thank_u_next.py

**4. Automated Login:** The program will automatically log in to each account, one by one, and navigate to the club moderation page.

**5. Manual Interaction (Optional):** The program will pause after each login. If needed, you can manually interact with the website. Simply press Enter to proceed to the next account.

**6. Automated Logout:** After visiting each club, the program will automatically log out and proceed to the next account.

**7. Completion:** Once the program has processed all accounts, it will display a completion message.

**Notes**
Ensure that you have a stable internet connection while running Thank-U-Next.

Double-check that the accounts.txt file is correctly formatted, with each username and password pair on separate lines.

Exercise caution when sharing or storing your accounts.txt file, as it contains sensitive information.


**Disclaimer**

Thank-U-Next is intended for personal use and should be used responsibly and in accordance with the terms of service of the platform it interacts with. It is not affiliated with or endorsed by Juni Learning or any other organization mentioned in this program.




