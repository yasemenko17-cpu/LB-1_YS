"""Автоматична перевірка варіанта 19."""
import pytest
from conftest import load
from kits import lab01

V = load(19)
CASES = [{'id': 'keys_gen',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': 'app_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': True}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'ufw_blocked_ip',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '10.5.5.100', 'port': 8443, 'iface': 'eth0'},
  'expect': 'DENY'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_19(case):
    lab01.check(V, case)
