Minchin.Text Changelog
======================

v 6.0.2 [2020-04-17]
--------------------

- fixed bug where ``progressbar`` would sometimes not calculated the needed bar
  length
- fixed display issue where is wasn't clear what the possible answers to
  queries were. This does make the output quite a bit longer.

v 6.0.1 [2020-04-10]
--------------------

- fixed alignment issues if you change the maximum value for ``progressbar``
- fixed ``progressbar`` numbers to be displayed with thousands commas, if large
  enough

v 6.0.0 [2019-02-08]
--------------------

- [BREAKING CHANGE] queries now return one of ``Answer.YES``, ``Answer.NO``,
  ``Answer.QUIT``, ``Answer.ALL``, or ``Answer.NONE``, as appropriate. ``YES``
  and ``ALL`` are "Truth-y", while ``NO``, ``QUIT``, and ``NONE`` are "False-y"
- added ``query_yes_no_all_none()``
- added ``rainbow_print()`` to print strings in all the colours!

v 5.1.1 [2017-10-03]
--------------------

- allow ``setup.py`` to work with versions of Python before 3.6
- remove hardcoded terminal width of 79 characters

v 5.1.0 [2017-01-29]
--------------------

- ``minchin.text.progressbar()`` will only print (by default) every 0.1 seconds
- fixed progressbar bug where "overfull" bars would go on to multiple lines
- added ``get_terminal_size()``
- upgraded release machinery

v 5.0 [2015-06-10]
------------------

- [BREAKING CHANGE] moved package to ``minchin.text``
- added tests for ``minchin.text.centered()``
- added end character to progress bar
- added documentation to README.rst

v 4.4 [2014-10-26]
------------------

- typographic changes to allow wmtext to work in Python 3

v 4.1 [2014-03-10]
------------------

- allow access as a direct object. i.e. use ``import wmtext`` rather than
  ``from wmtext import wmtext``

v 4.0 [2014-02-06]
------------------

- packaged as a separate module
- added progress bar
- first public release

v 3.2 [2014-02-02]
------------------

- add ``length_no_ansi()`` allowing you to determine the length of a string
  after stripping out ANSI codes.
