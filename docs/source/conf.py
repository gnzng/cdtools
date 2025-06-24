# -*- coding: utf-8 -*-
import os
import sys
import re

sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "CDTools"
copyright = "2019-2024, Abraham Levitan"
author = "Abraham Levitan"


def get_version():
    setup_py = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../setup.py")
    )
    with open(setup_py, "r") as f:
        content = f.read()
    version_match = re.search(r'version\s*=\s*[\'"]([^\'"]+)[\'"]', content)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string in setup.py.")


version = get_version()
release = version

html_title = f"{project} Documentation"

# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinxarg.ext",
    "sphinx_multiversion",
]

# sphinx-multiversion settings
smv_tag_whitelist = r"^v?\d+\.\d+.*$"
smv_branch_whitelist = r"^(main|master)$"
smv_remote_whitelist = None

# Theme - use classic instead of RTD
html_theme = "furo"

# Sidebar with versioning
html_sidebars = {
    "**": [
        "versioning.html",
    ],
}

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "_templates"]
pygments_style = "sphinx"


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "CDToolsdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#    (master_doc, 'CDTools.tex', 'CDTools Documentation',
#     'Abraham Levitan', 'manual'),
# ]
latex_documents = [
    ("latextoc", "CDTools.tex", "CDTools Documentation", "Abraham Levitan", "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "adcd", "ADCD Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "CDTools",
        "CDTools Documentation",
        author,
        "CDTools",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


autoclass_content = "both"
