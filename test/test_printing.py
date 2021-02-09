"""Centered visual test for `minchin.text`"""
import random

from minchin import text as wmtext


def test_centered():
    print(wmtext.centered("1. Basic"))
    print(wmtext.centered("2. Other Fill", fill="*"))
    print(wmtext.centered("3. Odd and Even Fill", fill="*"))
    print(wmtext.centered("3b. Odd and Even Fill", fill="*"))
    print(wmtext.centered("4. Multi Character Fill", fill="abc"))
    print(wmtext.centered("5. Short Line", 40, "*"))


def test_titles():
    wmtext.title("Testing Title")
    wmtext.subtitle("Almost as import text")


def test_rainbow():
    text = "0123456789" * 5
    for offset in range(7):
        wmtext.rainbow_print(text, offset)


def test_print_cols():
    wmtext.print_cols([random.randint(1, 1250) for _ in range(100)])
    wmtext.print_cols([random.randint(1, 1250) for _ in range(21)], cols=2)
    wmtext.print_cols([random.randint(1, 1250) for _ in range(100)], gap=10)
    wmtext.print_cols([random.randint(1, 1250) for _ in range(100)], indent=10)
    wmtext.print_cols([random.randint(1, 1250) for _ in range(100)], indent=10, gap=10)


if __name__ == "__main__":
    import colorama

    colorama.init()

    test_titles()
    print()
    test_centered()
    print()
    test_rainbow()
    print()
    test_print_cols()
