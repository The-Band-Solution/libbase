from typing import Generic, List, Optional, TypeVar

from libbase.services.generic_service import GenericService

T = TypeVar("T")


class GenericController(Generic[T]):
    """Generic controller facade for managing domain entities.

    This controller acts as the public interface (or facade) for the
    system, coordinating requests and delegating business logic to
    an underlying service implementation.
    """

    def __init__(self, service: GenericService[T]):
        """Initialize the generic controller.

        Args:
            service (GenericService[T]): The service implementation
                to be used for business logic coordination.
        """
        self._service = service

    def create(self, entity: T) -> None:
        """Create a new entity.

        Args:
            entity (T): The entity to be created.
        """
        self._service.create(entity)

    def get_by_id(self, entity_id: any) -> Optional[T]:
        """Retrieve an entity by its unique identifier.

        Args:
            entity_id (any): The unique identifier of the entity.

        Returns:
            Optional[T]: The entity if found, None otherwise.
        """
        return self._service.get_by_id(entity_id)

    def get_all(self) -> List[T]:
        """Retrieve all entities.

        Returns:
            List[T]: A list of all entities.
        """
        return self._service.get_all()

    def update(self, entity: T) -> None:
        """Update an existing entity.

        Args:
            entity (T): The entity with updated information.
        """
        self._service.update(entity)

    def delete(self, entity_id: any) -> None:
        """Remove an entity.

        Args:
            entity_id (any): The unique identifier of the entity to be removed.
        """
        self._service.delete(entity_id)
