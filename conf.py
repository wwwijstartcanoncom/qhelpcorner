# Configuration file for the Sphinx documentation builder.
 
import os
import sys
 
# -- Path setup --------------------------------------------------------------
 
# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))
 
# -- Project information -----------------------------------------------------
 
project = 'Download and Install Quicken Guide'
copyright = '2025, Quicken'
author = 'Quicken Support Team'
 
# The full version, including alpha/beta/rc tags
release = '1.0.0'
 
# -- HTML output settings ----------------------------------------------------
 
# Title shown in the browser tab and top of HTML pages
html_title = "How to Download and Install Quicken – Official Guide"
 
# Optional short title (e.g., for navigation bar or breadcrumb)
html_short_title = "Install Quicken"
 
# Favicon (place favicon.ico in the root or _static folder if used)
html_favicon = 'favicon.ico'
 
# Choose a theme (uncomment one if needed)
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'  # Recommended if you have multiple pages
 
# Hide "View page source" link
html_show_sourcelink = False
 
# Allow raw HTML blocks in .rst files (use with caution)
html_allow_unsafe = True
 
# Theme customization options (optional)
html_theme_options = {
    'show_powered_by': False,
    'collapse_navigation': False,
}
 
# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you use CSS, JS, or images
 
# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
