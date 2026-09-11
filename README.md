# openbis-parser-example

An example parser for openBIS using the bam-masterdata interface.

This repository is intended to be used as a template or example to be forked to generate new parsers in openBIS
integrated with the [`openbis-upload-helper`](https://github.com/BAMresearch/openbis-upload-helper).


## 1. Create a new parser repository

You can either [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) or [use this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) as a template.

Click on the button **Use this template** and choose **Create a new repository**:

<div align="center"><img width="900" alt="use-this-template" src="https://github.com/user-attachments/assets/4a6e244b-285c-4982-a576-7dcb69aa24fa" /></div>

You will be prompted to create a new repository. Choose:
- Place to host the repository (organization or your own profile). In our case, we selected _BAMResearch_
- Give a name.
- Write a short description.
- Choose _Public_ visibility.

<div align="center"><img width="600" alt="create-new-template" src="https://github.com/user-attachments/assets/bf509059-b734-4634-9e32-96b2c220b257" /></div>

## 2. Define your parser entry point

With your new repository created, clone it locally:
```bash
git clone https://github.com/BAMresearch/<name-of-the-parser-repo>.git
```

**Note**: we will be using our example with this repository to showcase the commands. Please, change the corresponding
paths to your own repository naming conventions.

We have now a new folder, `openbis-parser-example`, containing the following structure:
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

Below you can find an explanation of each file. You can also change the name of the package from `openbis_parser_example` to your preferred package name `<pkg-name>`.

In order to create your new parser, you have to:
1. Define a new class in `src/<pkg-name>/parser.py` instead of `OpenbisParserExample`. We recommend naming it `PkgName`.
2. Modify `src/<pkg-name>/__init__.py` entry point variables:
```python
from .parser import PkgName

# Add more metadata if needed
<pkg-name>_entry_point = {
    "name": "PkgName",
    "description": "A new parser for masterdata.",
    "parser_class": PkgName,
}
```
3. Modify the `pyproject.toml` line `[project.entry-points."bam.parsers"]` to the new entry point:
```sh
<pkg-name>_entry_point = "<pkg-name>:<pkg-name>_entry_point"
```
4. Modify all other parts in `pyproject.toml` where the `<pkg-name>` is `openbis_parser_example` to your package name.

## 3. Work in your parser

With the new structure, you can work in your parser to map data from your files into openBIS by modifying `src/<pkg-name>/parser.py` and the testing
module `tests/test_parser.py`.

## 4. Add new parser to `openbis-upload-helper`

Once your new parser has been developed and tested, you can add it to the registry of parsers in the [`openbis-upload-helper`](https://github.com/BAMresearch/openbis-upload-helper). We recommend you contacting the maintainers of the application with a link to your parser repository.
