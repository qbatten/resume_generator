from jinja2 import Template
import yaml

with open("resume.yml") as file:
    resume = yaml.safe_load(file)

#read your jinja template file
with open("main_template.html") as file:
    template = Template(file.read())


rendered = template.render(categories=resume['categories'])

with open('output.html', 'w') as f:
    f.write(rendered)
