"""Автоматична перевірка варіанта 24."""
import pytest
from conftest import load
from kits import lab01

V = load(24)
CASES = [{'id': 'ключі ed25519',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': '.ssh/id_ed25519.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'admin@gateway',
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': '.ssh/authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'files': {},
  'expect': {'allowgroups': ['sysadmins'], 'maxauthtries': ['3']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_24(case):
    lab01.check(V, case)
