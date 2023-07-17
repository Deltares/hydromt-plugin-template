from {{cookiecutter.project_slug}} import {{cookiecutter.model_name}}

def test_model_has_name():
    model = {{cookiecutter.model_name}}()
    assert hasattr(model,"_NAME")
