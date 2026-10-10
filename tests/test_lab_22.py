"""Автоматична перевірка варіанта 22."""
import pytest
from conftest import load
from kits import lab01

V = load(22)
CASES = [{'id': 'ключі rsa 4096',
  'public': True,
  'kind': 'keys',
  'args': [],
  'files': {},
  'expect': {'pubs': [{'path': '.ssh/id_rsa.pub',
                       'type': 'rsa',
                       'bits': 4096,
                       'comment': 'ldapadmin@dir-server',
                       'priv_mode': 384,
                       'pub_mode': 420,
                       'encrypted': False}],
             'authorized_keys': {'path': '.ssh/authorized_keys',
                                 'count': 1,
                                 'regex': ['^ssh-rsa '],
                                 'mode': 384}}},
 {'id': 'sshd суворий профіль',
  'public': True,
  'kind': 'sshd',
  'files': {},
  'expect': {'passwordauthentication': ['no'],
             'permitrootlogin': ['no'],
             'x11forwarding': ['no'],
             'allowtcpforwarding': ['no'],
             'permitemptypasswords': ['no'],
             'maxauthtries': ['2']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_22(case):
    lab01.check(V, case)
