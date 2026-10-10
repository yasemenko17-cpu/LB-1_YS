"""Автоматична перевірка варіанта 07."""
import pytest
from conftest import load
from kits import lab01

V = load(7)
CASES = [{'id': 'публічний тест ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'dns_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'dnsadmin@ns1',
                       'encrypted': True}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^from="10\\.0\\.0\\.100" ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'публічний тест ufw',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'udp', 'src': '8.8.8.8', 'port': 53, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_07(case):
    lab01.check(V, case)
