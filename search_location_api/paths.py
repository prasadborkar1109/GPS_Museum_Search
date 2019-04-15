import os


# Package main directory
PATH_PACKAGE = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
# Directory containing the package
PATH_ROOT = os.path.normpath(os.path.join(PATH_PACKAGE, os.pardir))
# Config directory
PATH_CONFIG = os.path.normpath(os.path.join(PATH_ROOT, 'config'))
