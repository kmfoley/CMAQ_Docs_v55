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
        'pydata_sphinx_theme']
myst_enable_extensions = ['colon_fence']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
source_suffix = {
        '.rst': 'restructuredtext',
        '.txt': 'restructuredtext',
        '.md': 'markdown'
        }


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
import pydata_sphinx_theme
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_baseurl = 'https://jbrunto.github.io/CMAQ_Docs_v55/'

html_sidebars = {'**': ['searchbar.html']}






