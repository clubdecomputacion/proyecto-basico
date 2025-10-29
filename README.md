# Proyecto Python con Tests, Pre-commit y GitHub Actions

Un proyecto Python de ejemplo que demuestra buenas prácticas de desarrollo incluyendo tests automatizados, pre-commit hooks y GitHub Actions para CI/CD.

## Estructura del Proyecto

```
proyecto/
├── main.py                    # código principal con funciones
├── tests/
│   ├── conftest.py            # configuración de pytest
│   └── test_main.py           # tests para las funciones
├── .pre-commit-config.yaml    # configuración de pre-commit
├── .github/
│   └── workflows/
│       └── checks.yml         # workflow de GitHub Actions
└── README.md
```

## Funcionalidades

El proyecto incluye dos funciones simples pero bien documentadas:

1. **`suma(a, b)`**: Calcula la suma de dos números
2. **`es_par(n)`**: Determina si un número es par

## Configuración de Desarrollo

### Prerrequisitos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/clubdecomputacion/proyecto-basico.git
cd proyecto-basico
```

2. Instala las dependencias:

```bash
pip install pytest ruff pre-commit
```

### Ejecutar el Programa

```bash
python main.py
```

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con detalles
pytest -v

# Ejecutar tests con cobertura
pytest --cov=.
```

## Pre-commit Hooks

### ¿Qué es Pre-commit?

[Pre-commit](https://pre-commit.com/) es un framework de *hooks* que se ejecutan automáticamente antes de cada `commit` para asegurar la calidad del código. Impide *commits* que no cumplan con los estándares definidos.

### Configuración Actual

El archivo `.pre-commit-config.yaml` configura los siguientes hooks:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace    # Elimina espacios en blanco al final
      - id: end-of-file-fixer      # Asegura nueva línea al final del archivo
      - id: check-yaml             # Valida sintaxis de archivos YAML
      - id: check-added-large-files # Previene commits de archivos muy grandes

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.0.275
    hooks:
      # Ejecutar el linter
      - id: ruff
        args: [ --fix, --exit-non-zero-on-fix ]  # Linter con auto-fix
      # Ejecutar el formateador
      - id: ruff-format                          # Formateador automático

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true                         # Ejecuta tests en cada commit
```

### Configurar Pre-commit

1. Instalar pre-commit:

```bash
pip install pre-commit
```

2. Instalar los hooks en el repositorio:

```bash
pre-commit install
```

3. Ejecutar manualmente pre-commit para todos los archivos, antes de realizar un commit:

```bash
pre-commit run --all-files
```

### Flujo de Trabajo con Pre-commit

1. Realizas cambios en el código
2. Ejecutas `git add .` para preparar los cambios
3. Al ejecutar `git commit`, los hooks se ejecutan automáticamente:
    - Si todos pasan: el commit se realiza
    - Si alguno falla: el commit se rechaza y debes corregir los errores

## GitHub Actions

### ¿Qué es GitHub Actions?

[GitHub Actions](https://github.com/features/actions) es una plataforma de CI/CD (Integración Continua/Despliegue Continuo) que automatiza *workflows* cada vez que ocurren eventos en el repositorio (push, pull request, etc.).

### Configuración Actual

El workflow definido en `.github/workflows/checks.yml` se activa al pushear tags que comienzan con 'v' (ej: v1.0.0, v2.1.3):

```yaml
name: Pre-commit Checks on Tags

on:
  push:
    tags:
      - 'v*'  # Se ejecuta solo en tags que empiezan con 'v'

jobs:
  quality-checks:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          pip install pytest ruff pre-commit

      - name: Run Ruff linter
        run: |
          ruff check --output-format=concise .

      - name: Run Ruff formatter
        run: |
          ruff format --check .

      - name: Run tests with pytest
        run: |
          pytest -v

      - name: Run all pre-commit hooks
        run: |
          pre-commit run --all-files
```

### Pasos del Workflow

1. **Checkout code**: Obtiene el código del repositorio
2. **Set up Python**: Configura Python 3.12
3. **Install dependencies**: Instala pytest, ruff y pre-commit
4. **Run Ruff linter**: Ejecuta el linter para verificar calidad de código
5. **Run Ruff formatter**: Verifica el formato del código
6. **Run tests**: Ejecuta todos los tests con pytest
7. **Run pre-commit hooks**: Ejecuta todos los hooks de pre-commit

### Ventajas de esta Configuración

- **Calidad asegurada**: El código cumple con estándares antes de cada release
- **Automático**: No requiere intervención manual
- **Rápido**: Se ejecuta solo en tags, no en cada push
- **Comprehensivo**: Incluye linting, formato y tests

## Herramientas Utilizadas

- [pytest](https://docs.pytest.org/): Framework de testing para Python
- [ruff](https://docs.astral.sh/ruff/): Linter y formateador rápido para Python
- [pre-commit](https://pre-commit.com/): Framework de gestión de hooks pre-commit
- [GitHub Actions](https://github.com/features/actions): Plataforma de CI/CD integrada con GitHub

## Desarrollo de Nuevas Funcionalidades

Al agregar nuevas funciones:

1. Escribe la función en `main.py` con documentación adecuada
2. Crea tests correspondientes en `tests/test_main.py`
3. Ejecuta `pytest` para verificar que los tests pasan
4. Ejecuta `pre-commit run --all-files` para verificar calidad de código
5. Realiza `git add`, `git commit` y `git push`

Para crear una nueva versión:

1. Asegúrate que todos los tests pasen localmente: `pre-commit run --all-files`
2. Realiza el `commit`
3. Crea un tag: `git tag v1.0.0` (incrementa según semver)
4. Push el tag: `git push origin v1.0.0`
5. GitHub Actions ejecutará automáticamente las verificaciones
6. Si todo pasa, el *tag* está listo para *release*

## Solución de Problemas

### Pre-commit falla

Si pre-commit falla al hacer commit:

- Revisa todos los mensajes de error
- Ejecuta `pre-commit run --all-files` para ver todos los errores
- Corrige los problemas manualmente si ruff no los arregla automáticamente
- Vuelve a hacer `git add .` y `git commit`

### Tests fallan en GitHub Actions

Si los tests fallan en CI pero pasan localmente:

- Verifica que las versiones de Python sean consistentes
- Asegúrate de haber instalado todas las dependencias necesarias
- Revisa diferencias entre entorno local y el runner de GitHub
