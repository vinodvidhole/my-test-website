from flask import Flask, render_template
from getdata import get_projects

app = Flask(__name__)

@app.route('/')
def hello_world():
  project_list = get_projects()
  return render_template('index.html',
                        project_list=project_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)