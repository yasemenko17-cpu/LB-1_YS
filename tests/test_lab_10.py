"""Автоматична перевірка варіанта 10."""
import pytest
from conftest import load
from kits import lab01

V = load(10)
CASES = [{'id': 'публічний тест ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'git_key.pub',
                       'type': 'rsa',
                       'bits': 4096,
                       'comment': 'git@repo',
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-rsa '],
                                 'mode': 384}}},
 {'id': 'публічний тест ufw',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '192.168.1.1', 'port': 9005, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_10(case):
    lab01.check(V, case)
