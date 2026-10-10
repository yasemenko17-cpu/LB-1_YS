"""Автоматична перевірка варіанта 18."""
import pytest
from conftest import load
from kits import lab01

V = load(18)
CASES = [{'id': 'keys_gen',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': 'container_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'comment': 'dockadmin@dock-node-05',
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'ufw_ssh_admin',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '192.168.50.10', 'port': 22, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_18(case):
    lab01.check(V, case)
