from jinja2 import Environment, FileSystemLoader

def generate_html_file(wines_dict, special_offers, age, year_suffix):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html') 
    rendered_html = template.render(wines_dict=wines_dict, special_offers=special_offers, age=age, year_suffix=year_suffix)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)
