from os.path import dirname, join, splitext
from jinja2 import Environment, FileSystemLoader
from textx import metamodel_from_file

this_folder = dirname(__file__)


def generate(calc_file, output_file=None):
    # Parse the .calc file into a model using the grammar
    calculator_mm = metamodel_from_file(join(this_folder, 'calculator.tx'))
    model = calculator_mm.model_from_file(calc_file)

    # Load the Jinja2 template
    env = Environment(loader=FileSystemLoader(this_folder),
                      trim_blocks=True, lstrip_blocks=True,
                      keep_trailing_newline=True)
    template = env.get_template('calculator.jinja')

    # Render the model to text
    code = template.render(model=model)

    if output_file is None:
        output_file = splitext(calc_file)[0] + '_generated.py'
    with open(output_file, 'w') as f:
        f.write(code)
    print(f"Generated {output_file}")


generate('expression.calc')