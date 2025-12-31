# Constitution: libbase

## 1. Vision statement
To provide a robust, enterprise-grade, and strictly architectural Python library for CRUD operations that can be seamlessly imported into larger applications. `libbase` serves as a foundational core for building scalable systems following Correct Software Engineering principles.

## 2. Core Values & Principles
- **DRY (Don't Repeat Yourself)**: Domain Entities and ORM Models should ideally be unified where pragmatism allows, avoiding duplicate class definitions.
- **TDD (Test Driven Development)**: All features must be defined by tests first. Code is written to pass tests and maintain a high standard of quality.
- **Full Documentation**: Every class and method must have a docstring explaining its purpose, arguments, and return values following Google Style.
- **Layered Architecture**: MVC + Service + Repository is preserved to ensure separation of concerns and maintainability.
- **SOLID**: Strict adherence to SOLID principles to ensure the library remains extensible and decoupled.

## 3. Technology Stack
- **Language**: Python 3.12+
- **Database Support**: SQLAlchemy (Sync) for SQL strategies, JSON files for lightweight storage.
- **Testing**: Pytest with Coverage
- **Linting**: Black, Flake8, and isort

## 4. Architecture Overview
- **Controller Layer**: Public Interface / Facade (Entry points).
- **Service Layer**: Pure Business Logic coordination.
- **Domain Layer**: Core entities and base definitions.
- **Infrastructure Layer**: Persistence strategies and generic repository implementations.

## 5. Methodology
- **Spec-Driven Development**: Requirements -> Technical Planning -> TDD Implementation -> Verification.
