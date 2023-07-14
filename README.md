# HydroMT plugin template

This is a template repository to help you get up to speed if you want to start your own HydroTM plugin.
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
  # For the sake of brevity, repos on GitHub can just use the 'gh' prefix
  $ cookiecutter gh:savente93/hydromt-plugin-template
  ```

  You will be asked some questions and the template will be generated for you! 

## Included in this template

- Working [pytest](https://github.com/pytest-dev/pytest)
- Recommended configuration of linters including
  - [ruff](https://github.com/astral-sh/ruff)
  - [black](https://github.com/psf/black)
  - [mypy](https://github.com/python/mypy)
- Configured [pre-commit](https://github.com/pre-commit/pre-commit) to make sure linters are enforced
- Default github actions for Testing, generating docs, and running pre-commit checks
- Quarto as docs generator