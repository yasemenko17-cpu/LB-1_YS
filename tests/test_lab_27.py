"""Автоматична перевірка варіанта 27."""
import pytest
from conftest import load
from kits import lab01

V = load(27)
CASES = [{'id': 'генерує ключ та authorized_keys',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'iot_key.pub', 'type': 'ed25519'}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^no-port-forwarding,no-pty ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'налаштування sshd',
  'public': True,
  'kind': 'sshd',
  'expect': {'permitrootlogin': ['prohibit-password'], 'maxsessions': ['2']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_27(case):
    lab01.check(V, case)
