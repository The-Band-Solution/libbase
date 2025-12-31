# Generic Specifications - libbase

## 1. Storage Guidelines

### 1.1 SQL Strategy (SQLAlchemy)
The `GenericSqlRepository` expects a SQLAlchemy declarative model mapped to a table with at least an `id` column.
- **Table Naming**: Flexible, determined by the consumer's model.
- **Primary Key**: Must support common types (Int, UUID, String).

### 1.2 JSON Strategy
- **File Structure**: A root dictionary where keys are entity IDs and values are serialized entity data.
- **Serialization**: Uses `dataclasses.asdict` by default.

## 2. Public API Specifications

### Class: `GenericController[T]`
Provides a simplified entry point for CRUD operations.
- `create(entity: T) -> None`
- `get_by_id(entity_id: any) -> Optional[T]`
- `get_all() -> List[T]`
- `update(entity: T) -> None`
- `delete(entity_id: any) -> None`

### Class: `GenericService[T]`
Coordinates business logic and acts as a bridge between the Controller and Repository.
- `create(entity: T) -> None`
- `get_by_id(id: any) -> Optional[T]`
- `get_all() -> List[T]`
- `update(entity: T) -> None`
- `delete(id: any) -> None`

### Interface: `IRepository[T]`
The base contract for all persistence implementations.
- `add(entity: T) -> None`
- `get_by_id(entity_id: any) -> Optional[T]`
- `get_all() -> List[T]`
- `update(entity: T) -> None`
- `delete(entity_id: any) -> None`

## 3. Extension Guidelines
To use `libbase` for a specific entity (e.g., `User`):
1.  Define a class inheriting from `libbase.domain.base.BaseEntity`.
2.  Initialize the desired Repository (e.g., `GenericSqlRepository(session, User)`).
3.  Inject the Repository into the `GenericService[User]`.
4.  Optionally use `GenericController[User]` as the public entry point.
