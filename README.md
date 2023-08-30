# HydroMT plugin template

This is a template repository to help you get up to speed if you want to start your own HydroMT plugin.
It is configured with most of the recommended best practices installed.

This template can be used using [cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Usage of the template
- Simple command line usage:

  ```bash
  $ pip install cookiecutter
  # Create project from the cookiecutter-pypackage.git repo template
  # You'll be prompted to enter values.
  # Then it'll create your Python package in the current working directory,
  # based on those values.
  $ cookiecutter https://github.com/savente93/hydromt-plugin-template
  ```

  You will be asked some questions and the template will be generated for you! 
  In those questions, suggestions will be shown to guide, just replace the word *plugin* 
  in the suggestions by your own plugin or model name (eg *anewmodel*) and the host 
  GitHub organisation or user from *Deltares* to your own name (eg *savente93*).

  Here are some detailed information about what each question implies:

  - project_name: The name of your GitHub project (this will be used as the title of your GitHub repository/README). Eg *HydroMT plugin*
  - project_slug: The slug of your project (this will be used as the name of the pypi/conda package). Eg *hydromt_plugin*
  - project_url: The url of your project (this will be used as the url of the github repository). Eg *https://github.com/Deltares/hydromt_plugin*
  - docs_url: The url of the documentation of your project (this will be used as the url of the documentation). Eg *https://deltares.github.io/hydromt_plugin*
  - model_classname: The name of the new HydroMT Model subclass that you are creating. Eg *PluginModel*
  - model_type: Type of HydroMT model corresponding to your model, one of [Model, GridModel, MeshModel, LumpedModel, NetworkModel] (!careful with syntax!)
  - model_shortname: The short name of your model. This will be used as the HydroMT Command Line name of your plugin and as the name of the main python file of your project (which will contain the definition of your new Model class). Eg *plugin*
  - project_tagline: A short tagline (short description phrase) for your project. Eg *A HydroMT plugin for plugin models.*
  - project_version: The version of your project. Eg *0.1.0*

## Included in this template

- Working [pytest](https://github.com/pytest-dev/pytest)
- Recommended configuration of linters including
  - [ruff](https://github.com/astral-sh/ruff)
  - [black](https://github.com/psf/black)
- Configured [pre-commit](https://github.com/pre-commit/pre-commit) to make sure linters are enforced
- Default github actions for Testing, generating docs, and running pre-commit checks
- [Quarto](https://quarto.org/docs/get-started/) as docs generator
