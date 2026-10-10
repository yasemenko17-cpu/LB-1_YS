"""Автоматична перевірка варіанта 09."""
import pytest
from conftest import load
from kits import lab01

V = load(9)
CASES = [{'id': 'публічний тест ключів',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'proxy_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'proxy@web',
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^no-port-forwarding,no-pty ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'публічний тест ufw',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '10.0.0.1', 'port': 80, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_09(case):
    lab01.check(V, case)
