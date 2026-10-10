"""Автоматична перевірка варіанта 23."""
import pytest
from conftest import load
from kits import lab01

V = load(23)
CASES = [{'id': 'ключі з from=',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': '.ssh/id_ed25519.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'mqadmin@broker-node',
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': '.ssh/authorized_keys',
                                 'count': 1,
                                 'regex': ['^from="192\\.168\\.100\\.0/24" ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'files': {},
  'expect': {'port': ['2222'], 'permitrootlogin': ['no'], 'passwordauthentication': ['no']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_23(case):
    lab01.check(V, case)
