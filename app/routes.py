from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def resume():
    # Define your resume data as a dictionary
    resume_data = {
        'name': 'Your Name',
        'email': 'your.email@example.com',
        'education': [
            {
                'degree': 'B.Sc. Computer Science',
                'institution': 'University of Example',
                'year': '2018 - 2022'
            }
        ],
        # Add more sections like skills, projects, experience, etc.
    }
    return render_template('resume.html', data=resume_data)
