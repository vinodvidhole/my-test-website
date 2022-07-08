import requests
import json

def get_projects():
  git_hub_projects = "https://api.github.com/users/vinodvidhole/repos"
  response = requests.get(git_hub_projects)
  
  if response.ok :
    project_data = json.loads(response.text)
  
  project_list = []
  for project in project_data:
      topic_list = []
      project_dict = {}
      topic_list = project["topics"]
      if len(topic_list) > 0 :
          topic_str = project["topics"][0] 
          if topic_str[:7] == "project":
              project_dict["html_url"] = project["html_url"]
              project_dict["description"] = project["description"]
              project_dict["image_url"] = project["homepage"]
              project_dict["filter"] = topic_str[8:]
              project_list.append(project_dict)
  return project_list
  