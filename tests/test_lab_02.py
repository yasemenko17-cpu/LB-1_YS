"""Автоматична перевірка варіанта 02."""
import pytest
from conftest import load
from kits import lab01

V = load(2)
CASES = [{'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'expect': {'allowusers': ['dba1', 'dba2'], 'x11forwarding': ['no'], 'allowtcpforwarding': ['no']}},
 {'id': 'ufw загальний стан',
  'public': True,
  'kind': 'ufw_state',
  'enabled': True,
  'default_in': 'deny',
  'default_out': 'allow',
  'rules_count': 2}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_02(case):
    lab01.check(V, case)
