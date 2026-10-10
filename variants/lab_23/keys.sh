#!/bin/bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Генеруємо ключ ed25519 без парольної фрази (-N "") та тихо (-q)
ssh-keygen -q -t ed25519 -N "" -C "mqadmin@broker-node" -f ~/.ssh/id_ed25519

# Встановлюємо жорсткі права 600 на приватний ключ
chmod 600 ~/.ssh/id_ed25519

# Додаємо публічний ключ у authorized_keys з опцією from=
PUBKEY=$(cat ~/.ssh/id_ed25519.pub)
echo "from=\"192.168.100.0/24\" $PUBKEY" > ~/.ssh/authorized_keys

# Встановлюємо правильні права доступу на authorized_keys
chmod 600 ~/.ssh/authorized_keys