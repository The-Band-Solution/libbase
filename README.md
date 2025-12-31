# libbase

Generic behavioral and architectural base library for enterprise applications.

## 🎯 Purpose
Deliver a standardized, robust, and well-tested architectural foundation for Python applications, ensuring consistency and quality across projects.

### Core Features:
- **Clean Architecture**: Strictly layered (Controller -> Service -> Repository).
- **Generic Repository Pattern**: Standardized CRUD operations for any entity.
- **Multi-Storage Strategy**: Out-of-the-box support for Memory, JSON files, and SQL (SQLAlchemy).
- **TDD-Ready**: Built following Test-Driven Development principles with 100% test focus.

## 🚀 Installation

### Stable Release (v0.1.0)
```bash
pip install git+https://github.com/The-Band-Solution/libbase.git@v0.1.0
```

### Development Version
```bash
pip install git+https://github.com/The-Band-Solution/libbase.git@main
```

## 🤝 Contributing
Please read [docs/MAINTENANCE.md](docs/MAINTENANCE.md) for detailed instructions on:
- **Quality Gates**: Using `Lefthook`.
- **Governance**: Creating Epics, Stories, and Tasks.
- **Standards**: TDD and DoD Verification.

## 📚 Documentation
Comprehensive documentation is available in the `docs/` folder:
- [Constitution](docs/constitution.md): Project vision and principles.
- [Design (SDD)](docs/sdd.md): Technical architecture and patterns.
- [Requirements](docs/requirements.md): Functional and non-functional specs.
- [Specifications](docs/specifications.md): API details and extension guides.
