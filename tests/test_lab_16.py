"""Автоматична перевірка варіанта 16."""
import pytest
from conftest import load
from kits import lab01

V = load(16)
CASES = [{'id': 'keys_gen',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': 'backup_key.pub',
                       'type': 'rsa',
                       'bits': 4096,
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-rsa '],
                                 'mode': 384}}},
 {'id': 'ufw_tcp_5050',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '192.168.1.100', 'port': 5050, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_16(case):
    lab01.check(V, case)
