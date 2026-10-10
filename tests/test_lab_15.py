"""Автоматична перевірка варіанта 15."""
import pytest
from conftest import load
from kits import lab01

V = load(15)
CASES = [{'id': 'створення ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'env': {},
  'files': {},
  'expect': {'pubs': [{'path': 'deploy_key.pub', 'type': 'ed25519', 'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^no-port-forwarding,no-pty ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'налаштування ufw',
  'public': True,
  'kind': 'ufw_state',
  'expect': {'enabled': True, 'default_in': 'deny', 'default_out': 'allow', 'rules_count': 3}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_15(case):
    lab01.check(V, case)
