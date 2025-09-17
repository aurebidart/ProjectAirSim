# Configuration file for the Sphinx documentation builder.

import os
import sys

import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath("../src"))

project = "Project AirSim"
copyright = "2022, Microsoft"
author = "Microsoft"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
]

autosummary_generate = True  # build autosummary pages
autodoc_typehints = "description"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# Si tu paquete importa libs pesadas / no disponibles en CI, mockealas:
autodoc_mock_imports = [
    "numpy", "cv2", "pynng", "airsim", "open3d", "torch", "ultralytics",
    # agregá acá cualquier otra dependencia que se importe a nivel de módulo
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
