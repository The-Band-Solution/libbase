import pytest

from libbase.infrastructure.interface import IRepository


def test_irepository_is_abstract():
    with pytest.raises(TypeError):
        IRepository()


def test_irepository_methods_exist():
    # This is more of a static check, but good for TDD flow
    assert hasattr(IRepository, "add")
    assert hasattr(IRepository, "get_by_id")
    assert hasattr(IRepository, "get_all")
    assert hasattr(IRepository, "update")
    assert hasattr(IRepository, "delete")
