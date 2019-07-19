import locale
import os

from contextlib import contextmanager


@contextmanager
def setlocale():
    saved = locale.setlocale(locale.LC_ALL)
    try:
        yield locale.setlocale(locale.LC_ALL, os.environ.get('LC_ALL',
                                                             'pt_BR.UTF-8'))
    finally:
        locale.setlocale(locale.LC_ALL, saved)
