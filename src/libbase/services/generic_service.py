from typing import Generic, List, Optional, TypeVar

from libbase.infrastructure.interface import IRepository

T = TypeVar("T")


class GenericService(Generic[T]):
    """Generic service layer for coordinating business logic.

    This service provides a standard interface for CRUD operations,
    delegating the actual persistence to an injected repository.
    """

    def __init__(self, repository: IRepository[T]):
        """Initialize the generic service.

        Args:
            repository (IRepository[T]): The repository implementation
                to be used for persistence.
        """
        self._repository = repository

    def create(self, entity: T) -> None:
        """Create a new domain entity.

        Args:
            entity (T): The entity to be created.
        """
        self._repository.add(entity)

    def get_by_id(self, entity_id: any) -> Optional[T]:
        """Retrieve an entity by its unique identifier.

        Args:
            entity_id (any): The unique identifier of the entity.

        Returns:
            Optional[T]: The entity if found, None otherwise.
        """
        return self._repository.get_by_id(entity_id)

    def get_all(self) -> List[T]:
        """Retrieve all entities.

        Returns:
            List[T]: A list of all entities.
        """
        return self._repository.get_all()

    def update(self, entity: T) -> None:
        """Update an existing entity.

        Args:
            entity (T): The entity with updated information.
        """
        self._repository.update(entity)

    def delete(self, entity_id: any) -> None:
        """Remove an entity.

        Args:
            entity_id (any): The unique identifier of the entity to be removed.
        """
        self._repository.delete(entity_id)
