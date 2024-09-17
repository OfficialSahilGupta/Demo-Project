## source-code

# This is a online online-voting-system

## Prerequisites 
above python 3.11.x

## Outline of folder
project-root/
│
├── config/                        # Configuration files for the online voting system
│   ├── online-voting-system.json  # Main configuration file (e.g., database, API keys, settings)
│   └── online-voting-system (2).json  # Possibly a backup or alternate configuration
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

## Outline for firestore database
## Firestore Database Structure

### Collections and Documents

#### 1. `candidates` Collection
This collection holds data related to each candidate in the election.

- **Document ID**: Auto-generated unique ID for each candidate (e.g., `1`, `2`, `3`, etc.).
- **Fields**:
  - `details`: (String) A description of the candidate (e.g., "He is a BTech grad from ...").
  - `image-link`: (String) A link to the candidate's profile picture or icon (e.g., `"https://www.flaticon.com/free-icon/alpha_13110717"`).
  - `name`: (String) The candidate's name (e.g., `"Alpha"`).

#### 2. `users` Collection
Each document in this collection represents a registered user in the system.

- **Document ID**: Auto-generated unique ID for each user.
- **Fields** (Assumed, not visible in the image):
  - Likely includes `username`, `email`, `role`, `createdAt`, etc., depending on your app's requirements.

#### 3. `vote-bank` Collection
This collection likely holds data related to voting transactions or records, such as votes cast by users for specific candidates.

- **Document ID**: Auto-generated unique ID for each voting record.
- **Fields** (Assumed, not visible in the image):
  - Could include references to `candidateId`, `userId`, `timestamp`, and other relevant fields.

---

### Example Structure in Firestore:

## This application uses Flask to communicate with firestore database  
# Setting Up the Virtual Environment
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
