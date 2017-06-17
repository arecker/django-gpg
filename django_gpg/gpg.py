import contextlib
import tempfile
import shutil

import gnupg


@contextlib.contextmanager
def client(import_keys=[]):
    tmp = tempfile.mkdtemp()
    try:
        g = gnupg.GPG(homedir=tmp)
        if import_keys:
            result = g.import_keys('\n'.join(import_keys))
            if 'IMPORT_OK 1' not in result.stderr:
                raise ValueError(result.stderr.split('\n')[0])
        yield g
    finally:
        shutil.rmtree(tmp)


def encrypt(message, recipient_keys=[]):
    if not recipient_keys:
        raise ValueError('Need at least one public key to encrypt to')
    with client(import_keys=recipient_keys) as g:
        keyids = [key['keyid'] for key in g.list_keys()]
        result = g.encrypt(message, ','.join(keyids))
        if not result.ok:
            raise ValueError(result.stderr.split('\n')[0])
        return result.data
