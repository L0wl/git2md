# 🔄 git2md

![PyPI](https://img.shields.io/pypi/v/git2md)
![Python Version](https://img.shields.io/pypi/pyversions/git2md)
![Build Status](https://img.shields.io/github/actions/workflow/status/xpos587/git2md/.github/workflows/release.yaml)
![License](https://img.shields.io/github/license/xpos587/git2md)
![AUR version](https://img.shields.io/aur/version/git2md-git)
🚀 Мощный инструмент командной строки для конвертации содержимого Git-репозиториев
в формат Markdown. Этот инструмент идеально подходит для разработчиков и специалистов
по документации, которым необходимо создавать структурированные Markdown-файлы
на основе содержимого репозиториев, включая дерево каталогов и содержимое файлов.

---

## ✨ Возможности

- **🌳 Генерация дерева каталогов репозитория**: выводит структуру репозитория в формате блока `tree`.
- **📝 Конвертация файлов в Markdown**:
  - Поддерживает подсветку синтаксиса для файлов с кодом.
  - ~~Конвертирует Jupyter Notebook (`.ipynb`) и PDF (`.pdf`) в Markdown.~~
- **🎯 Поддержка `.gitignore` и `.globalignore`**:
  - Автоматически исключает файлы/каталоги, указанные в `.gitignore` или `.globalignore`.
- **🔍 Пользовательские шаблоны исключений**: использование регулярных выражений для исключения определённых файлов или каталогов.
- **🗑️ Пропуск пустых файлов**: игнорирует файлы без содержимого.
- **🔢 Hexdump для бинарных файлов до 1 МБ**: небольшие бинарные файлы показываются в виде hex-таблицы.
- **📋 Копирование результата в буфер обмена**: упрощает использование сгенерированного Markdown.

---

## 🎬 Демонстрация

Ниже показана демонстрация работы `git2md`:

![Демонстрация git2md](https://raw.githubusercontent.com/Xpos587/git2md/refs/heads/main/assets/demo.gif)

---

## 📋 Требования

- **🐍 Python 3.9 или новее**
- **🐧 ~~Операционная система Linux~~ Теперь поддерживаются Windows, MacOS, Linux (X11 и Wayland)**
- **📦 Зависимости**:
  - `pathspec` (для поддержки `.gitignore`, `.mdignore`, `.globalignore`)
  - ~~`nbconvert` (для конвертации Jupyter Notebook)~~ (поддержка временно ограничена)
  - ~~`PyMuPDF4LLM` (для конвертации PDF)~~ (поддержка прекращена, будет заменена на лучшие аналоги)
  - `wl-copy/xsel/xclip` (опционально, только для Linux для функциональности буфера обмена)

---

## 📥 Установка

### 📦 Установка через PyPI

Вы можете установить `git2md` напрямую через PyPI, используя pip:

```bash
pip install git2md
```

### 🏗️ Установка через AUR (Arch Linux)

Для пользователей Arch Linux пакет доступен в AUR под именем [python-git2md](https://aur.archlinux.org/packages/python-git2md). Его можно установить с помощью помощников AUR, таких как `paru` или `yay`:

```bash
paru -S python-git2md
```

### 🔨 Установка из исходников

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/xpos587/git2md.git
   cd git2md
   ```

2. Сборка и установка:

   ```bash
   python setup.py build
   pip install .
   ```

---

## 🚀 Использование

### 💻 Базовая команда

```bash
git2md [путь] [опции]
```

Если путь не указан, будет использована текущая директория.

### ⚙️ Опции

| Опция            | Описание                                                              |
| ---------------- | --------------------------------------------------------------------- |
| `path`           | Путь к директории проекта или файлу Git (по умолчанию: текущая папка) |
| `-o`, `--output` | Путь для сохранения сгенерированного Markdown                         |
| `-c`, `--copy`   | Копировать результат в буфер обмена                                   |
| `--ignore`       | Список шаблонов для исключения файлов или каталогов                   |

---

## 📝 Примеры

### 📂 Генерация Markdown для всего репозитория

```bash
git2md /path/to/repo -o output.md
```

### 🔍 Исключение определённых файлов через шаблоны

```bash
git2md --ignore "./assets/style-*.css" "*.log" "*.tmp" -o output.md
```

### 🗑️ Копирование результата в буфер обмена

```bash
git2md --copy
```

---

## 📄 Формат вывода

### 🌳 Дерево директорий

Дерево директорий включено как блок кода с идентификатором языка `tree`. Например:

```tree
src/
├── main.py
├── utils/
│   ├── helper.py
│   └── __init__.py
└── README.md
```

### 📑 Содержимое файлов

Каждый файл включается с его относительным путём в заголовке, за которым следует его содержимое в блоке кода.

#### 🐍 Пример для Python-файла (`main.py`)

````markdown
# Файл: src/main.py

```
print("Hello, world!")
```

# Конец файла: src/main.py
````

#### 📓 Пример для Jupyter Notebook (`notebook.ipynb`)

Содержимое конвертируется из `.ipynb` в Markdown и включается напрямую:

```markdown
# Файл: notebook.ipynb

# Конвертированное содержимое из Jupyter Notebook...

# Конец файла: notebook.ipynb
```

#### 📄 Пример для PDF (`document.pdf`)

Текст извлекается в формате Markdown:

```markdown
# Файл: document.pdf

# Извлечённое содержимое из PDF...

# Конец файла: document.pdf
```

---

## 🔧 Глобальные шаблоны исключений

Вы можете создать файл `.mdignore` в той же директории, где находится скрипт, чтобы указать шаблоны, которые должны быть исключены для всех репозиториев. Формат идентичен `.gitignore`.

#### 📝 Пример `.mdignore`

```plaintext
__pycache__/
*.pyc
.mypy_cache/
.env
*.log
```

---

## 👨‍💻 Разработка

Для настройки среды разработки:

1. Создайте виртуальное окружение:

   ```bash
   micromamba create -p ./.micromamba/ -f environment.yml
   micromamba activate -p ./.micromamba/
   ```

2. Установите проект в режиме разработки:

   ```bash
   pip install -e .
   ```

---

## 📄 Лицензия

Этот проект лицензирован на условиях MIT License. Подробнее см. файл [LICENSE](LICENSE).

---

## 🤝 Вклад в проект

1. Форкните репозиторий.
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`).
3. Зафиксируйте изменения (`git commit -m 'Add some amazing feature'`).
4. Отправьте ветку в репозиторий (`git push origin feature/amazing-feature`).
5. Создайте Pull Request.

---

## 👥 Авторы

Michael (<x30827pos@gmail.com>)

---

## 🙏 Благодарности

Благодарим разработчиков [repomix](https://github.com/yamadashy/repomix) и [git2txt](https://github.com/mrauter1/git2txt).

Идея возникла из необходимости универсальной и упрощённой документации
репозиториев для рабочих потоков на основе LLM.
