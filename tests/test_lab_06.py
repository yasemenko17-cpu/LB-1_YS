"""Автоматична перевірка варіанта 06."""
import pytest
from conftest import load
from kits import lab01

V = load(6)
CASES = [{'id': 'публічний тест ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'fs_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'admin@fs.local',
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'публічний тест ufw',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '192.168.10.5', 'port': 2206, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_06(case):
    lab01.check(V, case)
