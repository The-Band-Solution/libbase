from dataclasses import dataclass

import pytest

from libbase.domain.base import BaseEntity
from libbase.infrastructure.memory_repository import GenericMemoryRepository
from libbase.services.generic_service import GenericService


@dataclass
class MockEntity(BaseEntity):
    name: str = ""


@pytest.fixture
def service():
    repo = GenericMemoryRepository[MockEntity]()
    return GenericService[MockEntity](repo)


def test_service_create(service):
    entity = MockEntity(id=1, name="Test")
    service.create(entity)

    result = service.get_by_id(1)
    assert result == entity


def test_service_get_all(service):
    service.create(MockEntity(id=1, name="One"))
    service.create(MockEntity(id=2, name="Two"))

    results = service.get_all()
    assert len(results) == 2


def test_service_update(service):
    entity = MockEntity(id=1, name="Old")
    service.create(entity)

    entity.name = "New"
    service.update(entity)

    result = service.get_by_id(1)
    assert result.name == "New"


def test_service_delete(service):
    service.create(MockEntity(id=1, name="Delete Me"))
    service.delete(1)

    result = service.get_by_id(1)
    assert result is None
