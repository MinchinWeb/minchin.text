REM Assumes is called from the root dirctory!
REM update pip, setuptools, wheel
pip install setuptools wheel pip -U
REM create distributions
python setup.py sdist
python setup.py bdist_egg
python setup.py bdsit_wheel
REM upload!
python setup.py sdist upload
python setup.py bdist_egg upload
python setup.py bdsit_wheel upload
