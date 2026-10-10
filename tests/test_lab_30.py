"""Автоматична перевірка варіанта 30."""
import pytest
from conftest import load
from kits import lab01

V = load(30)
CASES = [{'id': 'генерує ключ з коментарем',
  'public': True,
  'kind': 'keys',
  'args': [],
  'expect': {'pubs': [{'path': 'notify_key.pub', 'type': 'ed25519', 'comment': 'admin@notify'}]}},
 {'id': 'налаштування sshd',
  'public': True,
  'kind': 'sshd',
  'expect': {'allowgroups': ['notifyadmins'], 'maxauthtries': ['3']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_30(case):
    lab01.check(V, case)
