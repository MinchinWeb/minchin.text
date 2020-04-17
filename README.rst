minchin.text
============

Python library for text formatting on the command line.

Available Data
---------------

\_\_version\_\_
```````````````
library version.

re_ansi_control_codes
`````````````````````
Compiled regex pattern for ANSI control codes, including colors.

re_weburl
`````````
Compiled regex pattern for web URL's -- http, https, and naked domains like "example.com"

re_allurl
`````````
Compiled regex pattern to match all URL's, including "mailto:foo@example.com",
"x-whatever://foo", etc.

Answers
```````
An Enum containing the possible query answers. Current contains ``YES``,
``NO``, ``QUIT``, ``ALL``, and ``NONE``. ``YES`` and ``ALL`` are "truth-y"
while ``NO``, ``QUIT``, and ``NONE`` are "false-y".


Available Commands
------------------

length_no_ansi(mystring)
````````````````````````
Takes a string, strips out the ANSI escape codes
(used for colouring terminal output, etc.), and returns
the length of the resulting string

centered (mystring, linewidth=None, fill=" ")
`````````````````````````````````````````````
Takes a string, centres it, and pads it on both sides. Default ``linewidth`` is
one less than the console width.

clock_on_right(mystring)
````````````````````````
Takes a string, and prints it with the time right aligned

query_yes_no(question, default="yes")
`````````````````````````````````````
Ask a yes/no question via raw_input() and return their answer.

- "question" is a string that is presented to the user.
- "default" is the presumed answer if the user just hits <Enter>. It must be
  "yes" (the default), "no" or None (meaning an answer is required of the
  user).
- Returns one of Answer.YES or Answer.NO

query_yes_no_all(question, default="yes")
`````````````````````````````````````````
Ask a yes/no/all question via raw_input() and return their answer.

- "question" is a string that is presented to the user.
- "default" is the presumed answer if the user just hits <Enter>. It must be
  "yes" (the default), "no", "all" or None (meaning an answer is required of
  the user).
- Returns one of Answer.YES, Answer.NO, or Answer.ALL

def query_yes_quit(question, default="quit")
````````````````````````````````````````````
Ask a yes/quit question via raw_input() and return their answer.

- "question" is a string that is presented to the user.
- "default" is the presumed answer if the user just hits <Enter>. It must be
  "yes" (the default), "quit" or None (meaning an answer is required of the
  user).
- Returns one of Answer.YES or Answer.QUIT

query_yes_no_all_none(question, default="yes")
``````````````````````````````````````````````
Ask a yes/no/all/none question via raw_input() and return their answer.

- "question" is a string that is presented to the user.
- "default" is the presumed answer if the user just hits <Enter>. It must be
  "yes" (the default), "no", "all", "none" (i.e. the string) or None (meaning
  an answer is required of the user).
- Returns one of Answer.YES, Answer.NO, Answer.ALL, or Answer.NONE

wait(sec)
`````````
Prints a timer with the format 0:00 to the console,
and then clears the line when the timer is done.

title(mytitle)
``````````````
Takes ``mytitle``, centers it, and prints it in yellow letters on a blue
background.

subtitle(mysubtitle)
````````````````````
Takes ``mysubtitle``, centers it, and prints it in bright (white) letters on a
normal (black) background.

rainbow_print(text, offset=0)
`````````````````````````````
Prints out ``text`` in a cycle of rainbow-esque colors!


progressbar (class)
-------------------

This class is used to create and then update a 'progress bar', like:

.. code-block:: shell

    [================>                                                    ] 17 / 70


progressbar(current=0, maximum=100, bar_color=colorama.Fore.GREEN)
``````````````````````````````````````````````````````````````````
Creates a progress bar class. Prints the progress bar.

progressbar.update(currently=None)
``````````````````````````````````
Updates the value of the progress bar and prints it.

progressbar.reset()
```````````````````
Sets the value of the progress bar to 0 (zero) and prints it.

Code
----

The code is available at `https://github.com/MinchinWeb/minchin.text <https://github.com/MinchinWeb/minchin.text>`_

Contributions are welcome!

Tests
-----
Located in the `test` folder. Each is a "visual test", so they need to be run and the output manually examined.

License
-------
The code is licensed under the MIT license. See that attached `LICENSE` file.
