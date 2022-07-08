import requests
import json


def get_projects():
    git_hub_projects = "https://api.github.com/users/vinodvidhole/repos"
    response = requests.get(git_hub_projects)

    if response.ok:
        project_data = json.loads(response.text)

    project_list = []
    for project in project_data:
        topic_list = []
        project_dict = {}
        topic_list = project["topics"]
        if len(topic_list) > 0:
            topic_str = project["topics"][0]
            if topic_str[:7] == "project":
                project_dict["html_url"] = project["html_url"]
                project_dict["description"] = project["description"]
                project_dict["image_url"] = project["homepage"]
                project_dict["filter"] = topic_str[8:]
                project_list.append(project_dict)
    return project_list


def get_medium_blogs():
    
    medium_blogs = "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@vinodvidhole"
    blogs_icon_file = "https://gist.githubusercontent.com/vinodvidhole/3e20fc575f62e8cccda5d6b88cb1311f/raw/4113ccdc2d612700a7771e95d108cd0280fed083/blogs_icon.json"
    
    response_blogs = requests.get(medium_blogs)
    response_icons = requests.get(blogs_icon_file)    
    
    if response_icons.ok:
        blog_icon_data = json.loads(response_icons.text)
        
    if response_blogs.ok:
        blog_data = json.loads(response_blogs.text)

        blogs_list = []
        for blog in blog_data["items"]:
            blog_dict = {}
            
            blog_link = blog["link"]
            blog_dict["title"] = blog["title"]
            blog_dict["link"] = blog_link

            found = False
            for index, desc in enumerate(
                    blog['description'].split("</h4>")[:2]):
                if (index == 0) & (desc.upper().strip() == "<H4>DATA SCIENCE"):
                    found = True
                    continue
                else:
                    found = True
                if found:
                    blog_dict["description"] = desc[(desc.find('<h4>') + 4):].replace("&amp;", "and")
                    break
                    
            blog_dict["icon"] = list(filter(lambda item: item['link'] == blog_link, blog_icon_data))[0]['icon']        
            blogs_list.append(blog_dict)
                        
    return blogs_list
