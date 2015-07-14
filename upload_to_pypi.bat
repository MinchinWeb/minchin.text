REM Assumes is called from the root directory!
REM update pip, setuptools, wheel, twine
python -m pip install pip -U
pip install setuptools wheel twine -U
REM create distributions
python setup.py sdist bdist_egg bdsit_wheel
REM upload!
twine upload dist/*
