from flask import Flask, render_template, request, session, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['FIREBASE_CREDENTIALS'] = os.getenv('FIREBASE_CREDENTIALS')
app.config['UPLOAD_FOLDER'] = 'static/images/user_photos/'

# Initialize Firebase
cred = credentials.Certificate(app.config['FIREBASE_CREDENTIALS'])
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def home():
    return redirect(url_for('header'))  # Redirect to the header page

@app.route('/header')
def header():
    return render_template('header.html')  # Make sure you have 'header.html'

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        parent_name = request.form.get('parent_name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        aadhar = request.form.get('aadhar')
        
        if password != confirm_password:
            return "Passwords do not match", 400

        try:
            # Create a new user document in Firestore
            user_ref = db.collection('users').document(email)
            user_ref.set({
                'name': name,
                'dob': dob,
                'parent_name': parent_name,
                'email': email,
                'mobile': mobile,
                'password': password,
                'aadhar_number': aadhar,
                'photo_url': ''  # Initialize with an empty photo URL
            })
            
            return redirect(url_for('login'))
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    return render_template('registration.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user_ref = db.collection('users').document(email)
            user_data = user_ref.get()

            if user_data.exists:
                user = user_data.to_dict()
                
                # Check password (this should ideally be hashed and checked securely)
                if user.get('password') == password:
                    session['user_email'] = email
                    return redirect(url_for('personal_info'))
                else:
                    return "Invalid email or password", 401
            else:
                return "User not found", 404

        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    return render_template('login.html')


@app.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    if 'user_email' in session:
        user_email = session['user_email']
        
        try:
            user_ref = db.collection('users').document(user_email)
            user_data = user_ref.get()

            if user_data.exists:
                user_details = user_data.to_dict()
                
                if request.method == 'POST':
                    # Handle file upload and address update
                    if 'photo' in request.files:
                        photo = request.files['photo']
                        if photo:
                            photo_filename = secure_filename(photo.filename)
                            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
                            # Update Firestore with the new photo URL
                            user_ref.update({'photo_url': f'images/user_photos/{photo_filename}'})
                    
                    address = request.form.get('address')
                    if address:
                        user_ref.update({'address': address})

                return render_template('personal_info.html', 
                                       name=user_details.get('name'), 
                                       dob=user_details.get('dob'),
                                       parent_name=user_details.get('parent_name'),
                                       email=user_details.get('email'),
                                       mobile=user_details.get('mobile'),
                                       address=user_details.get('address'),
                                       aadhar=user_details.get('aadhar_number'),
                                       photo=user_details.get('photo_url'))
            else:
                return "User data not found in Firestore", 404
        
        except Exception as e:
            return f"An error occurred: {str(e)}", 500
    else:
        return redirect(url_for('login'))


@app.route('/election')
def election():
# Fetch and display election schedules
    return render_template('election.html')
@app.route('/rules')
def rules():
# Fetch and display rules
    return render_template('rules.html')


@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'GET':
        # Fetch candidates from Firestore
        candidates_ref = db.collection('candidates')
        candidates = candidates_ref.stream()

        # Convert Firestore documents to a list of dictionaries
        candidates_list = []
        for candidate in candidates:
            candidate_dict = candidate.to_dict()
            candidates_list.append(candidate_dict)

        # Render the vote page with candidates
        return render_template('vote.html', candidates=candidates_list)

    elif request.method == 'POST':
        # Get the selected candidate from the form
        selected_candidate = request.form['candidate']

        # Reference to the vote-bank collection's document for the selected candidate
        vote_ref = db.collection('vote-bank').document(selected_candidate)

        # Fetch the vote data
        vote_data = vote_ref.get()

        if vote_data.exists:
            # If candidate exists in vote-bank, update the vote count
            current_votes = int(vote_data.to_dict().get('votes', 0))
            new_votes = current_votes + 1

            # Update the vote count for the candidate
            vote_ref.update({'votes': str(new_votes)})
        else:
            # If the candidate doesn't exist in vote-bank, add with one vote
            vote_ref.set({'candidate': selected_candidate, 'votes': '1'})

        return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
