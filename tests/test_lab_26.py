"""Автоматична перевірка варіанта 26."""
import pytest
from conftest import load
from kits import lab01

V = load(26)
CASES = [{'id': 'генерує два ключі',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'main_key.pub', 'type': 'ed25519'},
                      {'path': 'backup_key.pub', 'type': 'rsa', 'bits': 4096}]}},
 {'id': 'налаштування sshd',
  'public': True,
  'kind': 'sshd',
  'expect': {'allowusers': ['dbadmin1', 'dbadmin2'], 'x11forwarding': ['no'], 'allowtcpforwarding': ['no']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_26(case):
    lab01.check(V, case)
