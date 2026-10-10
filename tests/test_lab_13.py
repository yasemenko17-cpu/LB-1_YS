"""Автоматична перевірка варіанта 13."""
import pytest
from conftest import load
from kits import lab01

V = load(13)
CASES = [{'id': 'створення ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'env': {},
  'files': {},
  'expect': {'pubs': [{'path': 'redis_key.pub', 'type': 'ed25519', 'encrypted': True}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'налаштування ufw',
  'public': True,
  'kind': 'ufw_state',
  'expect': {'enabled': True, 'default_in': 'deny', 'default_out': 'allow', 'rules_count': 3}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_13(case):
    lab01.check(V, case)
