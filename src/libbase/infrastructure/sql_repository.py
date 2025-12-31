from typing import List, Optional, Type, TypeVar

from sqlalchemy.orm import Session

from libbase.infrastructure.interface import IRepository

T = TypeVar("T")


class GenericSqlRepository(IRepository[T]):
    """SQLAlchemy-based implementation of the IRepository interface.

    This repository uses a SQLAlchemy Session to interact with a relational
    database. It assumes entities are mapped using SQLAlchemy's ORM.
    """

    def __init__(self, session: Session, entity_type: Type[T]):
        """Initialize the SQL repository.

        Args:
            session (Session): The SQLAlchemy session for database operations.
            entity_type (Type[T]): The class type of the entities being stored.
        """
        self._session = session
        self._entity_type = entity_type

    def add(self, entity: T) -> None:
        """Add a new entity to the repository.

        Args:
            entity (T): The domain entity to be added.
        """
        self._session.add(entity)
        self._session.commit()

    def get_by_id(self, entity_id: any) -> Optional[T]:
        """Retrieve an entity by its unique identifier.

        Args:
            entity_id (any): The unique identifier of the entity.

        Returns:
            Optional[T]: The entity if found, None otherwise.
        """
        return self._session.get(self._entity_type, entity_id)

    def get_all(self) -> List[T]:
        """Retrieve all entities from the repository.

        Returns:
            List[T]: A list of all entities in the repository.
        """
        return self._session.query(self._entity_type).all()

    def update(self, entity: T) -> None:
        """Update an existing entity in the repository.

        Args:
            entity (T): The entity with updated information.
        """
        self._session.merge(entity)
        self._session.commit()

    def delete(self, entity_id: any) -> None:
        """Remove an entity from the repository.

        Args:
            entity_id (any): The unique identifier of the entity to be removed.
        """
        entity = self.get_by_id(entity_id)
        if entity:
            self._session.delete(entity)
            self._session.commit()
