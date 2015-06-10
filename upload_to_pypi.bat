REM Assumes is called from the root dirctory!
REM update pip, setuptools, wheel, twine
pip install setuptools wheel twine pip -U
REM create distributions
python setup.py sdist bdist_egg bdsit_wheel
REM upload!
twine upload dist/*
