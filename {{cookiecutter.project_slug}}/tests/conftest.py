import pytest

import {{cookiecutter.project_slug}}


@pytest.fixture()
def random_number():
    return 4 # chosen by a fair dice roll.


@pytest.fixture()
def one():
    return 1

