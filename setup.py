
import os
import re
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

base_dir = os.path.dirname(os.path.abspath(__file__))

def get_version(filename="wmtext.py"):
    with open(os.path.join(base_dir, filename)) as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)

setup(
    name = "wmtext",
    version = get_version(),
    description = "Python library for text formatting on the command line.",
    long_description = "\n\n".join([open(os.path.join(base_dir, "README.md")).read(), open(os.path.join(base_dir,"HISTORY.md")).read()]),
    author = "W. Minchin",
    author_email = "w_minchin@hotmail.com",
    url = "https://github.com/MinchinWeb/wmtext",
	packages = find_packages(),
	include_package_data = True,
    install_requires = [
		"colorama >= 0.2.5"
        ],
    classifiers = (
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
        ),
)