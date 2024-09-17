## This is a online-voting-system application, we are using html, css, javascript, flask and firestore database. 

## Prerequisites 
above python 3.11.x installed to laptops

## Outline of folder
```
project-root/
│
├── config/                        # Configuration files for the online voting system
│   ├── online-voting-system.json  # Main configuration file (e.g., database, API keys, settings)
│
├── env/                           # Virtual environment for Python (contains installed packages)
│   └── ...                        # (No specific files shown, but this is where virtual environment files are)
│
├── static/                        # Contains static assets (CSS, JS, Images, etc.)
│   └── css
│   └── js/
|       └── script.js  
│   └── images/
|       └── user_photos/           # Stores user profile
|       └── default_user.png
├── templates/                     # Folder for HTML templates used by the Flask app
│   ├── about.html                 # Describes the voting system/platform
│   ├── base.html                  # Base layout template with shared structure (e.g., header, footer)
│   ├── election.html              # Displays election schedules or details
│   ├── header.html                # Common header file included in other templates
│   ├── login.html                 # Login page for user authentication
│   ├── personal_info.html         # Page for entering/editing personal information
│   ├── registration.html          # User registration page
│   ├── rules.html                 # Voting rules and regulations page
│   ├── thankyou.html              # Thank you/confirmation page after registration or voting
│   └── vote.html                  # Voting interface where users can cast votes
│
├── .env                           # Environment variable file (contains sensitive data like secrets, DB credentials)
│
├── .gitignore                     # Git configuration file, specifies files/folders to ignore in version control
│
├── app.py                         # Main Flask application file, defines routes, initializes the app
│
└── requirements.txt               # Lists Python dependencies (e.g., Flask, Jinja2, etc.)
```

You can link your application to own firebase project by generating your config file, add this config file to config/ directory and rename file to online voting system

## Firestore database structure
Collections and Documents

1. `candidates` Collection
- Purpose: Holds data related to each candidate in the election.
- Document ID: Auto-generated unique ID for each candidate (e.g., `1`, `2`, `3`, etc.).
- Fields:
  - `details`: (String) A description of the candidate 
  - `image-link`: (String) A link to the candidate's profile picture or icon 
  - `name`: (String) The candidate's name
  - 

2. `users` Collection
- Purpose: Represents registered users in the system.
- Document ID: Auto-generated unique ID for each user.
- Fields:
  - `aadhar_number`: (String) The user's Aadhar number.
  - `address`: (String) The user's address.
  - `dob`: (Timestamp) The user's date of birth.
  - `email`: (String) The user's email address.
  - `mobile`: (String) The user's mobile number.
  - `name`: (String) The user's name.
  - `parent_name`: (String) The name of the user's parent or guardian.
  - `password`: (String) The user's password (stored securely).
  - `photo_url`: (String) A URL to the user's profile photo.

3. `vote-bank` Collection
- Purpose: Holds data related to voting transactions or records.
- Document ID: Auto-generated unique ID for each voting record.
- Fields:
  - `candidate`: (String) Reference to the `candidates` collection, indicating the candidate who received the vote.
  - `votes`: (Number) The number of votes received by the candidate.
  
# Setting Up the Virtual Environment to start application
Follow these steps to create and activate a virtual environment using **virtualenv**.

# 1. Change terminal to working directory
```bash
cd src-code
```
# 2. Install `virtualenv` (if not already installed)
First, ensure you have `virtualenv` installed globally on your system:
```bash
pip install virtualenv
```

# 3. Creating virtual environment
```bash
virtualenv env
.\env\Scripts\activate
```

# 4. Start running flask program
```bash
python app.py
```

# 5. Install Project Dependencies
```bash
pip install -r requirements.txt
```
