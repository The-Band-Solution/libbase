# Agent Configuration - libbase

## 🏗 Technical Stack
- **Language**: Python 3.12+
- **Build System**: Hatchling (see `pyproject.toml`)
- **Main Dependencies**: SQLAlchemy 2.0+
- **Test Framework**: Pytest
- **Linting Tools**: Black, Flake8, isort

## 📂 Project Structure Map
- `src/libbase/domain/`: `BaseEntity` and core abstractions.
- `src/libbase/infrastructure/`: Repository strategies (SQL, JSON, Memory).
- `src/libbase/services/`: `GenericService`.
- `src/libbase/controllers/`: `GenericController`.
- `tests/`: TDD suite mimicking the `src/` structure.
- `docs/`: Full project documentation (SRS, SDD, Backlog, Milestones).

## ⚙️ Environment Commands
- **Install Dev**: `pip install -e ".[dev]"`
- **Test**: `pytest`
- **Lint**: `flake8 src tests`
- **Format**: `black src tests && isort src tests`
