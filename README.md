# mkdocs_temp
Шаблон проекта MkDocs

## Ссылки

- [MkDocs - Project documentation with Markdown](https://www.mkdocs.org/) &#127758;
- [mkdocs-sample](https://github.com/yriahi/mkdocs-sample) - Пример сайта документации
- [Example: Basic MkDocs project for Read the Docs](https://example-mkdocs-basic.readthedocs.io/)
- [example-mkdocs-basic](https://github.com/readthedocs-examples/example-mkdocs-basic)
- [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)

## Сборка проекта

```
$ rmvirtualenv mkdocs  # clean
$ mkvirtualenv mkdocs -p python3
(mkdocs) $ python -m pip install pip-tools
(mkdocs) $ cd mkdocs_temp
(mkdocs) $ pip-compile docs/requirements.in
(mkdocs) $ pip install -r docs/requirements.txt
(mkdocs) $ deactivate
```
- Сервер разработки
```
$ workon mkdocs
(mkdocs) $ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.06 seconds
INFO    -  [14:29:04] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [14:29:04] Serving on http://127.0.0.1:8000/
```
- [Открыть в браузере](http://127.0.0.1:8000/)
- Статический сайт
```
$ mkdocs build -s --no-directory-urls
```

## Команды

&#127758; [Command Line Interface](https://www.mkdocs.org/user-guide/cli/)

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

----