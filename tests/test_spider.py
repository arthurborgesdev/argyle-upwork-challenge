from spider import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_sum():
    assert 1 + 1 == 2