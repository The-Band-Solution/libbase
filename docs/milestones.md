# Milestones & Sprints - libbase

## Milestone: v0.1.0 - CRUD Foundation (Completed)
**Goal**: Establish the core architectural patterns and multi-storage repository strategies.

### Sprint 1: Infrastructure & Interface
- [x] TDD Environment (Pytest, Linting)
- [x] IRepository[T] Generic Interface
- [x] BaseEntity Definition

### Sprint 2: Storage Strategies
- [x] GenericMemoryRepository
- [x] GenericJsonRepository
- [x] GenericSqlRepository (SQLAlchemy)

### Sprint 3: Layered Architecture
- [x] GenericService[T]
- [x] GenericController[T] Facade
- [x] Documentation Standardizing (v0.1.0)

---

## Milestone: v0.2.0 - Advanced Querying & Async Support (Planned)
**Goal**: Expand the repository capabilities to support complex filtering and asynchronous operations.

### Planned Tasks:
- [ ] Specification Pattern for advanced queries.
- [ ] AsyncSQLRepository implementation.
- [ ] Pagination support in GenericService.
- [ ] Enhanced error handling and custom exceptions.
