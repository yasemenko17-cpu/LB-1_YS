"""Автоматична перевірка варіанта 21."""
import pytest
from conftest import load
from kits import lab01

V = load(21)
CASES = [{'id': 'ключі та authorized_keys',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': '.ssh/id_ed25519.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'mailadmin@mail.local',
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': '.ssh/authorized_keys',
                                 'count': 1,
                                 'regex': ['^no-port-forwarding,no-pty ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'files': {},
  'expect': {'permitrootlogin': ['prohibit-password'], 'maxsessions': ['2']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_21(case):
    lab01.check(V, case)
