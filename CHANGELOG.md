# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-12-31

### Added
- **Generic Repository Pattern**: `IRepository[T]` interface defining standard CRUD operations.
- **Multi-Storage Strategies**:
    - `GenericMemoryRepository`: In-memory storage for testing and fast prototyping.
    - `GenericJsonRepository`: Local JSON file persistence.
    - `GenericSqlRepository`: Relational database support via SQLAlchemy.
- **Domain Layer**: `BaseEntity` providing a unified identity for models.
- **Service Layer**: `GenericService[T]` for coordinating business logic.
- **Controller Layer**: `GenericController[T]` providing a facade interface for applications.
- **TDD Setup**: Full testing environment with `pytest`, `pytest-cov`, `black`, `flake8`, and `isort`.
- **CI/CD**: GitHub Actions for automated linting, testing, and release tagging.
- **Documentation**: Comprehensive architecture (`sdd.md`), requirements (`requirements.md`), and guidelines (`specifications.md`).

### Fixed
- Standardized docstrings to Google style across all core modules.
- Refined linting rules for better code consistency.
- Fixed specific `E501` and `F401` errors in repository and test files.
