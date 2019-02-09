- [BREAKING CHANGE] queries now return one of `Answer.YES`, `Answer.NO`,
  `Answer.QUIT`, `Answer.ALL`, or `Answer.NONE`, as appropriate. `YES` and
  `ALL` are "Truth-y", while `NO`, `QUIT`, and `NONE` are "False-y"
- added `query_yes_no_all_none()`
- added `rainbow_print()` to print strings in all the colours!


v 5.1.1 [2017-10-03]
====================

- allow `setup.py` to work with versions of Python before 3.6
- remove hardcoded terminal width of 79 characters

v 5.1.0 [2017-01-29]
====================

- `minchin.text.progressbar()` will only print (by default) every 0.1 seconds
- fix progressbar bug where "overfull" bars would go on to multiple lines
- add `get_terminal_size()`
- upgrade release machinery

v 5.0 [2015-06-10]
==================

- move package to `minchin.text`
- add tests for `minchin.text.centered()`
- add end character to progress bar
- add documentation to README.rst

v 4.4 [2014-10-26]
==================

- typographic changes to allow wmtext to work in Python 3

v 4.1 [2014-03-10]
==================

- allow access as a direct object. i.e. use `import wmtext` rather than `from wmtext import wmtext`

v 4.0 [2014-02-06]
==================

- packaged as a separate module
- added progress bar
- first public release
 
v 3.2 [2014-02-02]
==================

- add `length_no_ansi()` allowing you to determine the length of a string after stripping out ANSI codes.
