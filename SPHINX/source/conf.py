# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CMAQ_Documentation'
copyright = '2024, CMAQ Developers'
author = 'CMAQ Developers'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import sys, os
extensions = ['myst_parser',
        'sphinx.ext.githubpages',
        'sphinx_design',
        'pydata_sphinx_theme',
        'sphinx.ext.intersphinx',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosectionlabel']

autosectionlabel_prefix_document=True
myst_enable_extensions = ['colon_fence']
myst_heading_anchors = 1
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
source_suffix = {
        '.rst': 'restructuredtext',
        '.txt': 'markdown',
        '.md': 'markdown'
        }


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
import pydata_sphinx_theme
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_baseurl = 'https://jbrunto.github.io/CMAQ_Docs_v55/'

html_sidebars = {'**': ['globaltoc.html', 'searchbox.html']}


html_theme_options = {
    "github_url": "https://github.com/USEPA/CMAQ",
    "logo": {
        "image_light": "_static/CMAQ_Logo_2_inch.png",
        "image_dark": "_static/CMAQ_Logo_2_inch.png",
    "navigation_depth": 0
    }
}



