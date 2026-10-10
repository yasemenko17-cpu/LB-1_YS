"""Автоматична перевірка варіанта 08."""
import pytest
from conftest import load
from kits import lab01

V = load(8)
CASES = [{'id': 'публічний тест ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'mon_main.pub',
                       'type': 'rsa',
                       'bits': 2048,
                       'comment': 'main@mon',
                       'encrypted': False},
                      {'path': 'mon_backup.pub',
                       'type': 'rsa',
                       'bits': 2048,
                       'comment': 'backup@mon',
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 2,
                                 'regex': ['main@mon', 'backup@mon'],
                                 'mode': 384}}},
 {'id': 'публічний тест ufw',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '172.16.50.10', 'port': 9090, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_08(case):
    lab01.check(V, case)
