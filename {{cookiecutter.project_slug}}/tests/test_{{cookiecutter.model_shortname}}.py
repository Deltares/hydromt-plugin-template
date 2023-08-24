"""Testing {{cookiecutter.model_classname}} high level methods"""

from {{cookiecutter.project_slug}} import {{cookiecutter.model_classname}}


def test_model_has_name():
    model = {{cookiecutter.model_classname}}()
    assert hasattr(model, "_NAME")


def test_model_class():
    model = {{cookiecutter.model_classname}}()
    non_compliant = model._test_model_api()
    assert len(non_compliant) == 0, non_compliant
