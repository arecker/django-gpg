import contextlib
import tempfile
import shutil

import gnupg


@contextlib.contextmanager
def client():
    tmp = tempfile.mkdtemp()
    try:
        yield gnupg.GPG(homedir=tmp)
    finally:
        shutil.rmtree(tmp)
