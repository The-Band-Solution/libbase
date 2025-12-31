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


### ✅ Sprint 4: Foundation Standardization (v0.1.1)
- **Goal**: Finalize library infrastructure, Agile governance, and documentation standards.
- **Start Date**: 2025-12-31
- **End Date**: 2026-01-14
- **Focus**:
    - CI/CD with real package publishing.
    - Semantic Versioning automation.
    - Agile templates and governance setup.

---

## Milestone: v0.2.0 - Advanced Querying & Async Support (Planned)
**Goal**: Expand the repository capabilities to support complex filtering, pagination, and asynchronous operations.

### 🏃 Sprint 1 (v0.2.0): Advanced Capabilities
- **Start Date**: 2025-12-31
- **End Date**: 2026-01-14
- **Project**: The Band Project
- **Tasks**:
    - [ ] [Task] Implement Specification Pattern for Advanced Queries
    - [ ] [Task] Implement AsyncSQLRepository
    - [ ] [Task] Add Pagination Support
    - [ ] [Task] Enhance Error Handling and Custom Exceptions
