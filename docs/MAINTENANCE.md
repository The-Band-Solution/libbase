# Maintenance Context & AI Prompt Guide - libbase

This document serves as a "Universal Context" for any developer or AI coding assistant tasked with maintaining or extending `libbase`. It encapsulates the project's identity, architecture, and governance rules.

---

## 🚀 Project Identity: libbase
`libbase` is a generic architectural foundation library for enterprise Python applications. It provides standardized, strictly layered CRUD patterns.

### Core Architecture (Clean Architecture)
- **Layered Structure**: `Controller (Facade)` -> `Service (Business Logic)` -> `Repository (Persistence)`.
- **Generic Repository Pattern**: Uses `IRepository[T]` to decouple domain logic from storage.
- **Strategy Pattern**: Supports multiple backends (`Memory`, `JSON`, `SQLAlchemy`) switchable via configuration.
- **Domain Independence**: Entities inherit from `BaseEntity`.

---

## 🛠 Project configuration & Standards
- **Python**: 3.12+ (managed via `pyproject.toml`).
- **TDD Requirement**: **All changes must be driven by tests first.** No code is written without a corresponding test in `tests/`.
- **Documentation**: Google-style docstrings are mandatory for all classes and methods.
- **Code Style**: Strictly enforced by `black`, `flake8` (max-line-length: 88), and `isort`.
- **CI/CD**: GitHub Actions handle automated verification and tagging.

---

## 📋 Governance & Management
- **GitHub Issues**: Used for requirement tracking (Epics, US, Tasks).
- **Backlog**: Hierarchical tracking in `docs/backlog.md`.
- **Milestones**: Roadmap tracking in `docs/milestones.md`.
- **Changelog**: All versions documented in `CHANGELOG.md`.

---

## 🤖 AI Assistant "Super-Prompt"
If you are an AI assistant helping with this project, follow these instructions:

1.  **Context Loading**: Start by reading `docs/constitution.md`, `docs/sdd.md`, and `docs/specifications.md`.
2.  **TDD First**: Always check `tests/` before modifying `src/`. Propose tests before implementation.
3.  **Governance**: When starting a new feature, check `docs/backlog.md`. If a task doesn't exist, ask the user to create a GitHub Issue (or create one yourself if allowed).
4.  **Issue Association**: Every commit should ideally relate to a GitHub Issue (e.g., `feat: implementation #12`).
5.  **Documentation**: Keep all documentation in `docs/` synchronized with code changes.

---

## 📂 Key Locations
- `src/libbase/domain/`: Core base entities.
- `src/libbase/infrastructure/`: Repository strategies (Memory, JSON, SQL).
- `src/libbase/services/`: Generic business logic.
- `src/libbase/controllers/`: Application entry points.
- `tests/`: TDD suite.
