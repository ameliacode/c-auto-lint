# C++ Auto-Lint & Format

Automatically format and lint C++ files on commit using **clang-format** and **pre-commit** (Google style).

## Setup

### 1. Install

```bash
pip install pre-commit
```

### 2. Add `.clang-format`

```yaml
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 100
PointerAlignment: Left
```

### 3. Configure Pre-Commit

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-clang-format
    rev: v17.0.6
    hooks:
      - id: clang-format
        files: \.(cpp|hpp|cc|h)$
        args: [--style=file]
```

Install hook:

```bash
pre-commit install
```

### 4. Usage

```bash
git add main.cpp
git commit -m "Your message"
```

* Staged files will be auto-formatted before commit.

### 5. Optional Manual Run

```bash
pre-commit run clang-format --all-files
```
