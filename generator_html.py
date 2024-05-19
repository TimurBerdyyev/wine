from jinja2 import Environment, FileSystemLoader


def generate_html(wines_dict, age, year_suffix):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html') 
    rendered_html = template.render(wines_dict=wines_dict, age=age, year_suffix=year_suffix)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)
