'''Centered visual test for `minchin.text`'''
from minchin import text as wmtext

def test_centered():
    print(wmtext.centered('1. Basic'))
    print(wmtext.centered('2. Other Fill', fill='*'))
    print(wmtext.centered('3. Odd and Even Fill', fill='*'))
    print(wmtext.centered('3b. Odd and Even Fill', fill='*'))
    print(wmtext.centered('4. Multi Character Fill', fill='abc'))
    print(wmtext.centered('5. Short Line', 40, '*'))

if __name__ == "__main__":
    import colorama
    colorama.init()
    test_centered()
