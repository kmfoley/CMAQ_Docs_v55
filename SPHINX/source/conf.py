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
extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
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

html_sidebars = {}






