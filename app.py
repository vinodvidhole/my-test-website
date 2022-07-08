from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


git_hub_projects = "https://api.github.com/users/vinodvidhole/repos"
response = requests.get(git_hub_projects)

if response.ok :
  project_data = json.loads(response.text)

#print(project_data)
@app.route('/')
def hello_world():
  return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)