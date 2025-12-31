import json
import os
from dataclasses import dataclass

import pytest

from libbase.domain.base import BaseEntity
from libbase.infrastructure.json_repository import GenericJsonRepository


@dataclass
class MockEntity(BaseEntity):
    name: str = ""


@pytest.fixture
def test_json_file(tmp_path):
    return os.path.join(tmp_path, "test_repo.json")


def test_json_repository_add_and_get(test_json_file):
    repo = GenericJsonRepository[MockEntity](test_json_file, MockEntity)
    entity = MockEntity(id="1", name="Test")

    repo.add(entity)
    result = repo.get_by_id("1")

    assert result == entity
    assert result.name == "Test"

    # Check if file exists and has data
    assert os.path.exists(test_json_file)
    with open(test_json_file, "r") as f:
        data = json.load(f)
        assert "1" in data
        assert data["1"]["name"] == "Test"


def test_json_repository_get_all(test_json_file):
    repo = GenericJsonRepository[MockEntity](test_json_file, MockEntity)
    e1 = MockEntity(id="1", name="One")
    e2 = MockEntity(id="2", name="Two")

    repo.add(e1)
    repo.add(e2)
    results = repo.get_all()

    assert len(results) == 2
    assert any(e.name == "One" for e in results)
    assert any(e.name == "Two" for e in results)


def test_json_repository_update(test_json_file):
    repo = GenericJsonRepository[MockEntity](test_json_file, MockEntity)
    entity = MockEntity(id="1", name="Old")
    repo.add(entity)

    entity.name = "New"
    repo.update(entity)

    result = repo.get_by_id("1")
    assert result.name == "New"


def test_json_repository_delete(test_json_file):
    repo = GenericJsonRepository[MockEntity](test_json_file, MockEntity)
    entity = MockEntity(id="1", name="Delete Me")
    repo.add(entity)

    repo.delete("1")
    result = repo.get_by_id("1")

    assert result is None
    with open(test_json_file, "r") as f:
        data = json.load(f)
        assert "1" not in data
