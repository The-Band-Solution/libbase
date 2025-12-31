from dataclasses import dataclass

import pytest

from libbase.controllers.generic_controller import GenericController
from libbase.domain.base import BaseEntity
from libbase.infrastructure.memory_repository import GenericMemoryRepository
from libbase.services.generic_service import GenericService


@dataclass
class MockEntity(BaseEntity):
    name: str = ""


@pytest.fixture
def controller():
    repo = GenericMemoryRepository[MockEntity]()
    service = GenericService[MockEntity](repo)
    return GenericController[MockEntity](service)


def test_controller_create(controller):
    entity = MockEntity(id=1, name="Test")
    controller.create(entity)

    result = controller.get_by_id(1)
    assert result == entity


def test_controller_get_all(controller):
    controller.create(MockEntity(id=1, name="One"))
    controller.create(MockEntity(id=2, name="Two"))

    results = controller.get_all()
    assert len(results) == 2


def test_controller_update(controller):
    entity = MockEntity(id=1, name="Old")
    controller.create(entity)

    entity.name = "New"
    controller.update(entity)

    result = controller.get_by_id(1)
    assert result.name == "New"


def test_controller_delete(controller):
    controller.create(MockEntity(id=1, name="Delete Me"))
    controller.delete(1)

    result = controller.get_by_id(1)
    assert result is None
