"""{{cookiecutter.project_name}}: {{cookiecutter.project_tagline}}"""

from os.path import dirname, join, abspath

DATADIR = abspath(join(dirname(__file__), "data"))

from .{{ cookiecutter.model_shortname }} import {{cookiecutter.model_classname}}
