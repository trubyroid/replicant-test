import os
import sys

project = 'Voight-Kampff 3000'
copyright = '2023, Deckard'
author = 'Deckard'
release = '0.1'

sys.path.insert(0, os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage',
              'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
