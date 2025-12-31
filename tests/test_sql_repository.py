import pytest
from sqlalchemy import String, create_engine
from sqlalchemy.orm import (
    Mapped,
    declarative_base,
    mapped_column,
    sessionmaker,
)

from libbase.infrastructure.sql_repository import GenericSqlRepository

Base = declarative_base()


class MockEntity(Base):
    __tablename__ = "test_entities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_sql_repository_add_and_get(session):
    repo = GenericSqlRepository[MockEntity](session, MockEntity)
    entity = MockEntity(id=1, name="Test")

    repo.add(entity)
    result = repo.get_by_id(1)

    assert result == entity
    assert result.name == "Test"


def test_sql_repository_get_all(session):
    repo = GenericSqlRepository[MockEntity](session, MockEntity)
    e1 = MockEntity(id=1, name="One")
    e2 = MockEntity(id=2, name="Two")

    repo.add(e1)
    repo.add(e2)
    results = repo.get_all()

    assert len(results) == 2
    assert any(e.name == "One" for e in results)
    assert any(e.name == "Two" for e in results)


def test_sql_repository_update(session):
    repo = GenericSqlRepository[MockEntity](session, MockEntity)
    entity = MockEntity(id=1, name="Old")
    repo.add(entity)

    entity.name = "New"
    repo.update(entity)

    result = repo.get_by_id(1)
    assert result.name == "New"


def test_sql_repository_delete(session):
    repo = GenericSqlRepository[MockEntity](session, MockEntity)
    entity = MockEntity(id=1, name="Delete Me")
    repo.add(entity)

    repo.delete(1)
    result = repo.get_by_id(1)

    assert result is None
