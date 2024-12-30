#!/bin/bash

# Проверка доступности списка хостов

read -p "Введите через пробел IP или доменные имена хостов: " -a hosts

if [ ${#hosts[@]} -eq 0 ]; then
    echo "Ошибка: нет данных!"
    exit 1
fi

available_counter=0
unavailable_counter=0

for host in "${hosts[e]}"; do
    if ping -c 1 "$host" &> /dev/null; then
        echo "Хост $host доступен"
        ((available_counter++))
    else
        echo "Хост $host недоступен"
        ((unavailable_counter++))
    fi
done

echo "Всего доступных хостов: $available_counter"
echo "Всего недоступных хостов: $unavailable_counter"
