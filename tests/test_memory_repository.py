from dataclasses import dataclass

from libbase.domain.base import BaseEntity
from libbase.infrastructure.memory_repository import GenericMemoryRepository


@dataclass
class MockEntity(BaseEntity):
    name: str = ""


def test_memory_repository_add_and_get():
    repo = GenericMemoryRepository[MockEntity]()
    entity = MockEntity(id=1, name="Test")

    repo.add(entity)
    result = repo.get_by_id(1)

    assert result == entity
    assert result.name == "Test"


def test_memory_repository_get_all():
    repo = GenericMemoryRepository[MockEntity]()
    e1 = MockEntity(id=1, name="One")
    e2 = MockEntity(id=2, name="Two")

    repo.add(e1)
    repo.add(e2)
    results = repo.get_all()

    assert len(results) == 2
    assert e1 in results
    assert e2 in results


def test_memory_repository_update():
    repo = GenericMemoryRepository[MockEntity]()
    entity = MockEntity(id=1, name="Old")
    repo.add(entity)

    entity.name = "New"
    repo.update(entity)

    result = repo.get_by_id(1)
    assert result.name == "New"


def test_memory_repository_delete():
    repo = GenericMemoryRepository[MockEntity]()
    entity = MockEntity(id=1, name="Delete Me")
    repo.add(entity)

    repo.delete(1)
    result = repo.get_by_id(1)

    assert result is None


def test_memory_repository_get_non_existent():
    repo = GenericMemoryRepository[MockEntity]()
    result = repo.get_by_id(999)
    assert result is None
