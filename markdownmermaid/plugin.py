import re
import os
from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

try:
    unicode
except NameError:
    # Python 3 doesn't have `unicode` as `str`s are all Unicode.
    unicode = str


class MarkdownMermaidPlugin(BasePlugin):
    def on_page_markdown(self, md, page, config, **kwargs):
        def get_mmd_file(match):
            # .mmd file path should be relative to the "docs_dir" config
            docs_dir = config["docs_dir"]
            f_name = match[0]
            f_name = os.path.join(docs_dir, f_name.strip("`"))

            # Read the file and replace the `*.mmd` with
            # the contents in the file
            try:
                with open(f_name, "r") as mmd_file:
                    mmd_txt = mmd_file.read()

                # Wrap the file contents in the mermaid code tags and return
                return f"```mermaid\n{mmd_txt}\n```\n"
            except FileNotFoundError:
                # Return the an error with the file path to help user's debug
                return f"{f_name} does not exist"

        # markdown regex will look for file names *.mmd
        # inside single ` code tags
        # Example: `my_diagram.mmd`
        md_regex = r"`.*.mmd`"

        return re.sub(md_regex, get_mmd_file, md)

    def on_post_page(self, output_content, config, **kwargs):
        soup = BeautifulSoup(output_content, "html.parser")
        mermaids = soup.find_all("code", class_="mermaid")
        hasMermaid = 0
        for mermaid in mermaids:
            hasMermaid = 1
            # replace code with div
            mermaid.name = "div"
            # replace <pre>
            mermaid.parent.replace_with(mermaid)

        if hasMermaid == 1:
            new_tag = soup.new_tag("script")
            new_tag.string = "mermaid.initialize();"
            soup.body.append(new_tag)

        return unicode(soup)
