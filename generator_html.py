from jinja2 import Environment, FileSystemLoader
from reader import excel_file
from year_suffix import year_suffix
from vines_age import vinery_age


def generate_html():
    file_path = 'wine.xlsx'
    vines = excel_file(file_path)
    winery_age = vinery_age()
    year_suffixs = year_suffix(winery_age)
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html') 
    rendered_html = template.render(vines=vines, winery_age=winery_age, year_suffix=year_suffixs)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)
