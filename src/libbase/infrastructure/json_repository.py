import json
import os
from dataclasses import asdict
from typing import Dict, List, Optional, Type, TypeVar

from libbase.domain.base import BaseEntity
from libbase.infrastructure.interface import IRepository

T = TypeVar("T", bound=BaseEntity)


class GenericJsonRepository(IRepository[T]):
    """JSON file-based implementation of the IRepository interface.

    This repository persists entities to a JSON file. It handles
    serialization of dataclasses and deserialization back into
    the specified entity type.
    """

    def __init__(self, file_path: str, entity_type: Type[T]):
        """Initialize the JSON repository.

        Args:
            file_path (str): The path to the JSON file used for storage.
            entity_type (Type[T]): The class type of the entities being stored.
        """
        self._file_path = file_path
        self._entity_type = entity_type
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Create the JSON file with an empty dict if it doesn't exist."""
        if not os.path.exists(self._file_path):
            with open(self._file_path, "w") as f:
                json.dump(
                    {},
                    f,
                )

    def _load_data(self) -> Dict[any, dict]:
        """Load all data from the JSON file.

        Returns:
            Dict[any, dict]: A dictionary of raw entity data.
        """
        try:
            with open(self._file_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save_data(self, data: Dict[any, dict]) -> None:
        """Save raw data to the JSON file.

        Args:
            data (Dict[any, dict]): The data to be saved.
        """
        with open(self._file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add(self, entity: T) -> None:
        """Add a new entity to the repository.

        Args:
            entity (T): The domain entity to be added.
        """
        data = self._load_data()
        data[str(entity.id)] = asdict(entity)
        self._save_data(data)

    def get_by_id(self, entity_id: any) -> Optional[T]:
        """Retrieve an entity by its unique identifier.

        Args:
            entity_id (any): The unique identifier of the entity.

        Returns:
            Optional[T]: The entity if found, None otherwise.
        """
        data = self._load_data()
        raw_entity = data.get(str(entity_id))
        if raw_entity:
            return self._entity_type(**raw_entity)
        return None

    def get_all(self) -> List[T]:
        """Retrieve all entities from the repository.

        Returns:
            List[T]: A list of all entities in the repository.
        """
        data = self._load_data()
        return [self._entity_type(**item) for item in data.values()]

    def update(self, entity: T) -> None:
        """Update an existing entity in the repository.

        Args:
            entity (T): The entity with updated information.
        """
        data = self._load_data()
        str_id = str(entity.id)
        if str_id in data:
            data[str_id] = asdict(entity)
            self._save_data(data)

    def delete(self, entity_id: any) -> None:
        """Remove an entity from the repository.

        Args:
            entity_id (any): The unique identifier of the entity to be removed.
        """
        data = self._load_data()
        str_id = str(entity_id)
        if str_id in data:
            del data[str_id]
            self._save_data(data)
