from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BaseEntity:
    """Base class for all domain entities.

    Attributes:
        id (Optional[any]): The unique identifier of the entity.
    """

    id: Optional[any] = field(default=None, init=True)
