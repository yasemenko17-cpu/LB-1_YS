"""Автоматична перевірка варіанта 04."""
import pytest
from conftest import load
from kits import lab01

V = load(4)
CASES = [{'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'expect': {'passwordauthentication': ['no'], 'pubkeyauthentication': ['yes'], 'maxauthtries': ['2']}},
 {'id': 'ufw загальний стан',
  'public': True,
  'kind': 'ufw_state',
  'enabled': True,
  'default_in': 'deny',
  'rules_count': 4}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_04(case):
    lab01.check(V, case)
