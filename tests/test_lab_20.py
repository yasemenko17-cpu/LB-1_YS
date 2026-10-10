"""Автоматична перевірка варіанта 20."""
import pytest
from conftest import load
from kits import lab01

V = load(20)
CASES = [{'id': 'keys_gen_two',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': 'primary_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False},
                      {'path': 'backup_key.pub',
                       'type': 'ed25519',
                       'bits': 256,
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': 'authorized_keys',
                                 'count': 2,
                                 'regex': ['^ssh-ed25519 '],
                                 'mode': 384}}},
 {'id': 'ufw_limit_ssh',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '10.0.0.5', 'port': 22, 'iface': 'eth0'},
  'expect': 'ALLOW'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_20(case):
    lab01.check(V, case)
