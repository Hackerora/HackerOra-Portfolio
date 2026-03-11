from flask import Flask, jsonify

app = Flask(__name__)

projects = [
"Port Scanner in C",
"Password Cracker in Python",
"Network Scanner using Bash",
"Cybersecurity Tools Collection"
]

@app.route("/projects")
def get_projects():
    return jsonify(projects)

app.run(port=5000)