{!README.md!}

# Документация SuperDuperPython

Здравствуйте! Это документация для SuperDuperPython v1.3.6, последнее обновление <u>25 окт. 2017</u>.

## Документация для SuperDuperPython и платы Duper

Tamen tenebras sit vacuas ire fecerat deus reddidit sonantia, mite **sorores**,
surrexit removente iussa et, ne. Verba malorum Lycias tempestiva irae ex mentes
illo durasse Proteus genitore habes; Phoebes doloris, **et rara**.

!!! info
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

## Cross-references

- [Cross-references to any Markdown heading](https://mkdocstrings.github.io/usage/#cross-references-to-any-markdown-heading)
- Please see the [Install - step 3][install-step-3] section &#128279;


## Примеры кода 
### Bash

```bash
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

```

### Python

```python
import flask
import flask_saml

app = flask.Flask(__name__)

app.config.update({
    'SECRET_KEY': 'soverysecret',
    'SAML_METADATA_URL': 'https://mymetadata.xml',
})
flask_saml.FlaskSAML(app)
```
### C & C++

```c
#include <stdio.h>

int main(void) {
    printf("Hello world!\n"); // example output
}
```

```c++
#include <iostream>

int main() {
  std::cout << "Hello world!" << std::endl;
  return 0;
}
```



### Структура проекта

```bash
├── docs
│   ├── about.md
│   └── index.md
├── mkdocs.yml
└── site
    ├── 404.html
    ├── about
    │   └── search_index.json
    ├── sitemap.xml
    └── sitemap.xml.gz

```

### JSON

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```