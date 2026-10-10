"""Автоматична перевірка варіанта 25."""
import pytest
from conftest import load
from kits import lab01

V = load(25)
CASES = [{'id': 'ключі з парольною фразою',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': '.ssh/id_ed25519.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'student@lab-stand',
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': True}],
             'authorized_keys': {'path': '.ssh/authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'files': {},
  'expect': {'logingracetime': ['30'], 'clientaliveinterval': ['120'], 'clientalivecountmax': ['2']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_25(case):
    lab01.check(V, case)
