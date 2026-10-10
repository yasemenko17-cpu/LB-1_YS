"""Автоматична перевірка варіанта 11."""
import pytest
from conftest import load
from kits import lab01

V = load(11)
CASES = [{'id': 'створення ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'env': {},
  'files': {},
  'expect': {'pubs': [{'path': 'vpn_key.pub', 'type': 'ed25519', 'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^from="10\\.8\\.0\\.0/24" ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'налаштування ufw',
  'public': True,
  'kind': 'ufw_state',
  'expect': {'enabled': True, 'default_in': 'deny', 'default_out': 'allow', 'rules_count': 2}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_11(case):
    lab01.check(V, case)
