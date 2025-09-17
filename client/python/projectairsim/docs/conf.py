# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path
import sphinx_rtd_theme

# ====== Paths ======
HERE = Path(__file__).resolve()
SRC = (HERE.parent / "../src").resolve()  # .../client/python/projectairsim/src
sys.path.insert(0, str(SRC))

project = 'Project AirSim'
copyright = '2022, Microsoft'
author = 'Microsoft'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

# Mockeá deps que no están en CI (evita fallos de import)
autodoc_mock_imports = [
    'cryptography', 'airsim', 'cv2', 'numpy', 'pandas', 'scipy', 'torch', 'matplotlib'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'  # ✅ NO uses get_html_theme_path (deprecado)
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]  # ❌ eliminar esta línea