"""Автоматична перевірка варіанта 14."""
import pytest
from conftest import load
from kits import lab01

V = load(14)
CASES = [{'id': 'створення ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'env': {},
  'files': {},
  'expect': {'pubs': [{'path': 'main_key.pub', 'type': 'ed25519', 'encrypted': False},
                      {'path': 'backup_key.pub', 'type': 'ed25519', 'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 2,
                                 'regex': ['ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'налаштування ufw',
  'public': True,
  'kind': 'ufw_state',
  'expect': {'enabled': True, 'default_in': 'deny', 'default_out': 'allow', 'rules_count': 2}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_14(case):
    lab01.check(V, case)
