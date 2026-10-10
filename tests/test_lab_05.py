"""Автоматична перевірка варіанта 05."""
import pytest
from conftest import load
from kits import lab01

V = load(5)
CASES = [{'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'expect': {'port': ['2222'], 'permitrootlogin': ['no'], 'passwordauthentication': ['no']}},
 {'id': 'ufw загальний стан',
  'public': True,
  'kind': 'ufw_state',
  'enabled': True,
  'default_in': 'deny',
  'rules_count': 1}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_05(case):
    lab01.check(V, case)
