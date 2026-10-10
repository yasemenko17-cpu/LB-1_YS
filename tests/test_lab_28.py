"""Автоматична перевірка варіанта 28."""
import pytest
from conftest import load
from kits import lab01

V = load(28)
CASES = [{'id': 'генерує ключ cctv_key',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'cctv_key.pub', 'type': 'rsa', 'bits': 4096}]}},
 {'id': 'налаштування sshd',
  'public': True,
  'kind': 'sshd',
  'expect': {'permitrootlogin': ['no'], 'passwordauthentication': ['no'], 'maxauthtries': ['2']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_28(case):
    lab01.check(V, case)
