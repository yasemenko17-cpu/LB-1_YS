#!/bin/bash
# Скидання та встановлення базових політик
ufw --force reset
ufw default deny incoming
ufw default allow outgoing

# Трафік на eth1 для підмережі 192.168.100.0/24 до портів 5672 та 15672
ufw allow in on eth1 from 192.168.100.0/24 to any port 5672
ufw allow in on eth1 from 192.168.100.0/24 to any port 15672

# SSH на порт 2222/tcp з підмережі 192.168.100.0/24 (без зазначення інтерфейсу)
ufw allow from 192.168.100.0/24 to any port 2222 proto tcp

# Увімкнення фаєрвола
ufw --force enable