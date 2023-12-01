from flask import Flask, jsonify
from config import CVData
import click, json

cv_data = CVData()
app = Flask(__name__)

def handle_missing_key(data, key, default=None):
    """Handle missing keys by providing a default value or returning an error response."""
    return data.get(key, default)

# RESTful API endpoints
@app.route('/personal', methods=['GET'])
def get_personal_info():
    personal_info = handle_missing_key(cv_data.data, "personal_info", {})
    return jsonify(personal_info)

@app.route('/experience', methods=['GET'])
def get_experience():
    experience_data = handle_missing_key(cv_data.data, "experience_data", [])
    return jsonify(experience_data)

@app.route('/education', methods=['GET'])
def get_education():
    education_data = handle_missing_key(cv_data.data, "education_data", [])
    return jsonify(education_data)

@app.route('/skills', methods=['GET'])
def get_skills():
    skills_data = handle_missing_key(cv_data.data, "skills_data", [])
    return jsonify(skills_data)

@app.route('/certifications', methods=['GET'])
def get_certifications():
    certifications_data = handle_missing_key(cv_data.data, "certifications_data", [])
    return jsonify(certifications_data)

# CLI command
@app.cli.command("get-cv")
def print_cv_data():
    response = {
        "Personal Info": handle_missing_key(cv_data.data, "personal_info", {}),
        "Experience": handle_missing_key(cv_data.data, "experience_data", []),
        "Education": handle_missing_key(cv_data.data, "education_data", []),
        "Skills": handle_missing_key(cv_data.data, "skills_data", []),
        "Certifications": handle_missing_key(cv_data.data, "certifications_data", [])
    }

    click.echo(json.dumps(response, indent=4))


if __name__ == '__main__':
    app.run(debug=False)
