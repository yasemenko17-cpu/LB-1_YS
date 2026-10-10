"""Автоматична перевірка варіанта 29."""
import pytest
from conftest import load
from kits import lab01

V = load(29)
CASES = [{'id': 'генерує ключ та authorized_keys',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'jupyter_key.pub', 'type': 'ed25519'}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^from=\\"192\\.168\\.50\\.0/24\\" ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'налаштування sshd',
  'public': True,
  'kind': 'sshd',
  'expect': {'port': ['2222'], 'permitrootlogin': ['no'], 'passwordauthentication': ['no']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_29(case):
    lab01.check(V, case)
