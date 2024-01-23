# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# This will include the necessary source files folders in the PATH to be able to generate the documentation from.
# devdir=r'C:\Users\parkm\Desktop\git\ExceptionNotifier'
# try:
#     if os.environ['DEVDIR']:
#         devdir = os.environ['DEVDIR']
# except KeyError:
#     print('Unable to obtain $DEVDIR from the environment.')
#     pass

sys.path.insert(0, os.path.abspath("../.."))
sys.setrecursionlimit(1500)


# Ensure that the __init__ method gets documented.
def skip(app, what, name, obj, skip, options):
    if name == "__init__":
        return False
    return skip


# -- Project information -----------------------------------------------------

project = "bardapi"
copyright = "2024, minwoo park"
author = "minwoo park"

# The full version, including alpha/beta/rc tags
release = "0.1.39"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.todo"]

# ,'sphinx.ext.napoleon'

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
todo_include_todos = True
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
