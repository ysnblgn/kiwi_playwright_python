import pytest
from pytest_bdd import scenario

@pytest.mark.T1
@scenario("../features/basic_search.feature", "T1 - One way flight search")
def test_basic_search():
    pass