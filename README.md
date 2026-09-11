# openbis-parser-example

Example parser for openBIS using the `bam-masterdata` parser interface.

This repository can be used as a template for creating new parsers that can be used with the [`openbis-upload-helper`](https://github.com/BAMresearch/openbis-upload-helper).


## 1. Create a new parser repository

You can either [fork this repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) or [use it as a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

Click **Use this template** and choose **Create a new repository**:

<div align="center"><img width="900" alt="use-this-template" src="https://github.com/user-attachments/assets/4a6e244b-285c-4982-a576-7dcb69aa24fa" /></div>

Choose:

- the organization or profile where the repository will be created;
- a repository name;
- a short description;
- the desired visibility.

At BAM, parsers are typically hosted under the [`BAMresearch`](https://github.com/BAMresearch) organization.

<div align="center"><img width="600" alt="create-new-template" src="https://github.com/user-attachments/assets/bf509059-b734-4634-9e32-96b2c220b257" /></div>


## 2. Define your parser

Clone your new repository:

```bash
git clone https://github.com/BAMresearch/<repository-name>.git
```

**Note**: The examples below use this repository's current package name, openbis_parser_example. Replace it with your own repository name where needed.

The repository has the following structure:

```sh
openbis-parser-example
├── LICENSE
├── pyproject.toml
├── README.md
├── src
│   ├── openbis_parser_example
│       ├── __init__.py
│       ├── parser.py
│       └── _version.py
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_parser.py
```

To create your parser:

1. Define your parser class in `src/<package-name>/parser.py`. The class **must** inherit from the `bam-masterdata` parser interface, `AbstractParser`.
2. Expose the parser in `src/<package-name>/__init__.py`:

```python
from .parser import MyParser

my_parser_entry_point = {
    "name": "My Parser",
    "description": "Description of the parser.",
    "parser_class": MyParser,
}
```

3. Register the parser in `pyproject.toml`:

```sh
[project.entry-points."bam.parsers"]
my_parser = "<package-name>:my_parser_entry_point"
```

4. Update the remaining package-specific values in `pyproject.toml`, such as the project name, package paths, URLs, and `setuptools-scm` configuration.

## 3. Implement and test the parser

Implement the parsing logic in:

```sh
src/<package-name>/parser.py
```

Add or update tests in:

```sh
tests/test_parser.py
```

The parser should transform the source files into `bam-masterdata` objects that can later be written to openBIS.

## 4. Use the parser with `openbis-upload-helper`

Once the parser is developed, tested, and released as a Python package, it can be included as a dependency of the [`openbis-upload-helper`](https://github.com/BAMresearch/openbis-upload-helper).

`openbis-upload-helper` automatically discovers installed parsers registered under the bam.parsers entry-point group.

If the parser should be included in the distributed application, contact the `openbis-upload-helper` maintainers and provide the parser repository and released package version.