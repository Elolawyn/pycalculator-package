# pycalculator-package

Paquete de prueba de python que ofrece una calculadora.

## Documentación

* [Registro de Cambios](CHANGELOG.md).
* [Código de Conducta](CODE_OF_CONDUCT.md).
* [Guía de Contribución](CONTRIBUTING.md).
* [Licencia](LICENSE).
* [Política de Seguridad](SECURITY.md).
* [Soporte](SUPPORT.md).

## Instalación

* Ejecutar tarea `🔁 Nuevo entorno`.
* Ejecutar tarea `📦 Instalar`.

Alternativamente, en consola.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
pip install -e
```

## Actualizar dependencias

* Editar `requirements.in` o `requirements-dev.in`.
* Ejecutar tarea `📥 Actualizar`.
* Ejecutar tarea `📦 Instalar`.

Alternativamente, en consola.

```bash
source .venv/bin/activate
pip-compile --strip-extras --output-file=requirements/prod.txt requirements.in
pip-compile --output-file=requirements/dev.txt requirements-dev.in
pip install -r requirements/dev.txt
```

## Comprobar guía de estilo

* Ejecutar tarea `🔍 Lint`.

Alternativamente, en consola.

```bash
ruff check src tests
```

## Ejecutar tests

* Ejecutar tarea `🧪 Tests`.

Alternativamente, en consola.

```bash
pytest
```

## Comprobar cobertura

* Ejecutar tarea `📊 Cobertura`.

Alternativamente, en consola.

```bash
# Windows
cmd /c start htmlcov\\index.html
# Linux
xdg-open htmlcov/index.html
# MacOS
open htmlcov/index.html
```

## Construir paquete

* Ejecutar tarea `🛠 Construir`.

Alternativamente, en consola.

```bash
source .venv/bin/activate
python -m build
```

## Desplegar a TestPyPi

* Debe existir fichero `.pypirc`:

```
[distutils]
index-servers =
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-TOKEN
```

* Ejecutar tarea `🚀 TestPyPI`.

Alternativamente, en consola.

```bash
source .venv/bin/activate
twine upload --repository testpypi dist/*
```
