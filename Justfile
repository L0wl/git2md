project_dir := "."
env_prefix := "micromamba run -p ./.micromamba"

# Проверить код на ошибки
lint:
    {{env_prefix}} black --check --diff {{project_dir}}
    {{env_prefix}} ruff check {{project_dir}}
    {{env_prefix}} mypy {{project_dir}} --strict

# Запустить форматировщик кода
reformat:
    {{env_prefix}} black {{project_dir}}
    {{env_prefix}} ruff format {{project_dir}}

# Запустить проект
run:
    {{env_prefix}} python -m src.git2md || true

# Установить зависимости
install_requirements:
    {{env_prefix}} pip install -r requirements.txt

# Запустить будущие тесты
test:
    {{env_prefix}} pytest

# Собрать будущую документацию
docs:
    sphinx-build -b html docs/source docs/build

# Установить проект в систему
install_local:
    {{env_prefix}} pip install -e .

# Очистить кэш и временные файлы
clean:
    find . -name "__pycache__" -exec rm -rf {} +
    find . -name "*.pyc" -exec rm -f {} +
    rm -rf build dist .eggs .tox .nox .coverage .hypothesis .pytest_cache

# Обновить версию в PKGBUILD и setup.py
update_version version:
    sed -i "s/version=\"[0-9\.]\+\"/version=\"{{version}}\"/" setup.py
    sed -i "s/^pkgver=[0-9\.]\+/pkgver={{version}}/" PKGBUILD
    echo "Version updated to {{version}}"
