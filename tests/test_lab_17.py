"""Автоматична перевірка варіанта 17."""
import pytest
from conftest import load
from kits import lab01

V = load(17)
CASES = [{'id': 'keys_gen',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': 'ftp_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^from="172\\.16\\.10\\.0/24" ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'ufw_ftp_eth1',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '10.0.0.5', 'port': 21, 'iface': 'eth1'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_17(case):
    lab01.check(V, case)
