# -*- coding: utf-8 -*-
# -- Project information -----------------------------------------------------

from recommonmark.parser import CommonMarkParser
project = "Python Scritping in Jupiter"
author = "TechnoStar Co. Ltd"
copyright = "2002-2020, " + author
scv_greatest_tag = True
scv_banner_greatest_tag = True
scv_show_banner = True

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # standard sphinx extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
    "sphinx_tabs.tabs",
    "sphinx_panels",
    "sphinx_copybutton",
    # "sphinx_thebe",
    "sphinx_togglebutton",

    # cloud's extensions
    'cloud_sptheme.ext.autodoc_sections',
    'cloud_sptheme.ext.index_styling',
    'cloud_sptheme.ext.relbar_toc',
    'cloud_sptheme.ext.escaped_samp_literals',
    'cloud_sptheme.ext.issue_tracker',
    'cloud_sptheme.ext.table_styling',

    # other extensions
    "numpydoc",
    "jupyter_sphinx",
    "myst_nb",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "cloud"
html_logo = "_static/logo.png"
html_short_title = "Python Script in Jupiter"

# Material theme options (see theme.conf for more information)
html_theme_options = {
    "roottarget": "get_started",
    "max_width": "12in",
    "borderless_decor": True,
    "collapsiblesidebar": False,
}

html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html"]
}

# html_context = {
#     "github_user": "Musashi7",
#     "github_repo": "PSJ",
#     "github_version": "material_theme",
#     "doc_path": "docs",
# }

html_css_files = [
    'stylesheets/custom.css',
]

# html_js_files = [
#     'javascript/amplify.js',
# ]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom parameters
myst_amsmath_enable = True
myst_admonition_enable = True
myst_html_img_enable = True
myst_dmath_enable = True
myst_deflist_enable = True
myst_figure_enable = True
myst_url_schemes = ("http", "https", "mailto")
myst_heading_anchors = 2
# panels_add_boostrap_css = False
myst_dmath_enable = True
numfig = True
autosummary_generate = True
html_show_sphinx = False
show_authors = False
pygments_style = 'sphinx'
autodoc_member_order = "bysource"
html_show_sourcelink = False

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# The frontpage document.
index_doc = 'get_started'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ["cloud_sptheme."]

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# Use markdown as default content, instead of rst
source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
