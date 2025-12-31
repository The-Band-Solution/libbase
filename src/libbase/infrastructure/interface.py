from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class IRepository(ABC, Generic[T]):
    """Generic interface for the Repository pattern.

    This interface defines the standard CRUD operations that all repository
    implementations must provide. It uses a generic type T representing
    the domain entity.
    """

    @abstractmethod
    def add(self, entity: T) -> None:
        """Add a new entity to the repository.

        Args:
            entity (T): The domain entity to be added.
        """
        pass

    @abstractmethod
    def get_by_id(self, entity_id: any) -> Optional[T]:
        """Retrieve an entity by its unique identifier.

        Args:
            entity_id (any): The unique identifier of the entity.

        Returns:
            Optional[T]: The entity if found, None otherwise.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Retrieve all entities from the repository.

        Returns:
            List[T]: A list of all entities in the repository.
        """
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        """Update an existing entity in the repository.

        Args:
            entity (T): The entity with updated information.
        """
        pass

    @abstractmethod
    def delete(self, entity_id: any) -> None:
        """Remove an entity from the repository.

        Args:
            entity_id (any): The unique identifier of the entity to be removed.
        """
        pass
