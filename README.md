# mkdocs-markdownextradata-plugin

A MkDocs plugin that render meraid graph to mermaid style


## Installation


Install the package with pip:

```bash
pip install mkdocs-mermaid-plugin
```

## Usage

Enable this plugin in your `mkdocs.yml`:

```yaml
plugins:
    - markdownmermaid

extra_javascript:
    - https://unpkg.com/mermaid/dist/mermaid.min.js
```

> **Note:** Don't forget to include the mermaid.min.js (local or remotely) in your `mkdocs.yml`

### Read from .mmd files

Sometimes mermaid diagrams can get quite large and having them inline with your main markdown doc can make it hard to manage. If you prefer to keep your diagrams in seperate `.mmd` files, you can put the file path to your `.mmd` file where you would like to insert the diagram.

#### Example

If you have have a file `my_diagram.mmd` in a `diagrams` directory inside your `docs` directory
> **Note:** The search path is inside of the `docs_dir` for your config, so be sure you path is relative to that which is `docs` by default.

```markdown
# My Markdown file

`diagrams/my_diagram.mmd`

```

The `diagrams/my_diagram.mmd` will be replaced in the build with the contents of the file.

> **Note:** Don't mermaid code block tags inside the mmd file. The plugin with do this automatically for you.

More information about plugins in the [MkDocs documentation][mkdocs-plugins]

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
