"""Автоматична перевірка варіанта 03."""
import pytest
from conftest import load
from kits import lab01

V = load(3)
CASES = [{'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'expect': {'permitrootlogin': ['prohibit-password'], 'maxsessions': ['2']}},
 {'id': 'ufw загальний стан',
  'public': True,
  'kind': 'ufw_state',
  'enabled': True,
  'default_in': 'deny',
  'rules_count': 2}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_03(case):
    lab01.check(V, case)
