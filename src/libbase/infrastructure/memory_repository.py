from typing import Dict, List, Optional, TypeVar

from libbase.domain.base import BaseEntity
from libbase.infrastructure.interface import IRepository

T = TypeVar("T", bound=BaseEntity)


class GenericMemoryRepository(IRepository[T]):
    """In-memory implementation of the IRepository interface.

    This repository uses a dictionary to store entities in RAM. It is
    primarily intended for testing and prototyping. Entities must
    inherit from BaseEntity to ensure they have an 'id' attribute.
    """

    def __init__(self):
        """Initialize the in-memory repository."""
        self._storage: Dict[any, T] = {}

    def add(self, entity: T) -> None:
        """Add a new entity to the repository.

        Args:
            entity (T): The domain entity to be added.
        """
        self._storage[entity.id] = entity

    def get_by_id(self, entity_id: any) -> Optional[T]:
        """Retrieve an entity by its unique identifier.

        Args:
            entity_id (any): The unique identifier of the entity.

        Returns:
            Optional[T]: The entity if found, None otherwise.
        """
        return self._storage.get(entity_id)

    def get_all(self) -> List[T]:
        """Retrieve all entities from the repository.

        Returns:
            List[T]: A list of all entities in the repository.
        """
        return list(self._storage.values())

    def update(self, entity: T) -> None:
        """Update an existing entity in the repository.

        Args:
            entity (T): The entity with updated information.
        """
        if entity.id in self._storage:
            self._storage[entity.id] = entity

    def delete(self, entity_id: any) -> None:
        """Remove an entity from the repository.

        Args:
            entity_id (any): The unique identifier of the entity to be removed.
        """
        if entity_id in self._storage:
            del self._storage[entity_id]
