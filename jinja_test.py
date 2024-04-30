from jinja2 import Template

name = "feodor"

tm = Template('noroc {{ name }}')
msg = tm.render(name=name)

print(msg)
