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
'''
def get_medium_blogs():
  medium_blogs = "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@vinodvidhole"
  response = requests.get(medium_blogs)
  
  if response.ok:
    blog_data = json.loads(response.text)

    blogs_list = []
    for blog in blog_data["items"]:
      blog_dict = {}

      blog_dict["title"] = blog["title"]
      blog_dict["link"] = blog["link"]

      found = False 
      for index, desc in enumerate(blog['description'].split("</h4>")[:2]):
          if (index == 0) & (desc.upper().strip() == "<H4>DATA SCIENCE") :
              found = True
              continue
          else:
              found = True
          if found:    
              blog_dict["description"] = desc[(desc.find('<h4>')+4):]
              break;    
      blogs_list.append(blog_dict)      
  return blogs_list
'''   
  