import jinja2
import os

content = ""

with open("template.html",'r') as f:
    html_template = str(f.read()) 
    template= jinja2.Template(html_template)
    print("DERP")
    files = os.listdir("audio")
    files.sort()
   
    content = template.render({'files':files})
     

with open("index.html",'w') as f:
    
    f.write(content)