# mkdocs_temp
Шаблон проекта MkDocs

## Ссылки

- [MkDocs - Project documentation with Markdown](https://www.mkdocs.org/) &#127758;
- [mkdocs-sample](https://github.com/yriahi/mkdocs-sample) - Пример сайта документации
- [Example: Basic MkDocs project for Read the Docs](https://example-mkdocs-basic.readthedocs.io/)
- [example-mkdocs-basic](https://github.com/readthedocs-examples/example-mkdocs-basic)
- [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)

## Сборка проекта

This project has a standard MkDocs layout which is built by Read the Docs almost the same way that you would build it locally (on your own laptop!).

You can build and view this documentation project locally - we recommend that you activate [a local Python virtual environment first](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment):

```console
# Install required Python dependencies (MkDocs etc.)
pip install -r docs/requirements.txt

# Run the mkdocs development server
mkdocs serve
# Build the MkDocs documentation
mkdocs build -s --no-directory-urls
```

&#9989; Open up [http://127.0.0.1:8000](http://127.0.0.1:8000/) in your browser.

## Команды

&#127758; [Command Line Interface](https://www.mkdocs.org/user-guide/cli/)

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

----