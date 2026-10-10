"""Автоматична перевірка варіанта 01."""
import pytest
from conftest import load
from kits import lab01

V = load(1)
CASES = [{'id': 'sshd конфігурація',
  'public': True,
  'kind': 'sshd',
  'expect': {'logingracetime': ['30'], 'clientaliveinterval': ['120'], 'clientalivecountmax': ['2']}},
 {'id': 'ufw загальний стан',
  'public': True,
  'kind': 'ufw_state',
  'enabled': True,
  'default_in': 'deny',
  'rules_count': 4}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_01(case):
    lab01.check(V, case)
