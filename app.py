from flask import Flask, request, jsonify
import git # This is from the GitPython library in your list
import os
import shutil

app = Flask(__name__)

@app.route('/')
def home():
    return "Builder App is Online! Send a repo URL to /build"

@app.route('/build', methods=['POST'])
def build_repo():
    # This is where your user would "put a repo"
    repo_url = request.json.get('repo_url')
    if not repo_url:
        return jsonify({"error": "No URL provided"}), 400

    return jsonify({"message": f"Received {repo_url}. Ready to clone!"})

if __name__ == '__main__':
    # The pipeline will run this and wait 5 seconds
    app.run(host='0.0.0.0', port=5000)