# -*- coding: utf-8 -*-

__author__ = 'Geislor Crestani'
__email__ = 'geislor@gmail.com'
__version__ = '0.1.3'
from .menu import general
import os
import sys
__all__ = ('general',)

abspath = lambda *p: os.path.abspath(os.path.join(*p))
CONFIG_DIR = abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(CONFIG_DIR)
PROJECT_ROOT = os.path.dirname(CONFIG_DIR)
sys.path.insert(0, os.path.join(PROJECT_DIR, "apus"))

