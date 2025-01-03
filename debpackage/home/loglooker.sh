#!/bin/bash

read -p "Введите путь к директориям с логами: " logs_dir
read -p "Введите ключевое слово для поиска: " keyword

if [ ! -d "$logs_dir" ]; then
	echo "Ошибка: папка $logs_dir не найдена!"
	exit 1
fi

line_counter=0

shopt -s nullglob
for log_file in "$logs_dir"/*.log; do
	if [ -f "$log_file" ]; then
		lines=$(grep -c "$keyword" "$log_file" 2> /dev/null)
		if [ $? -ne 0 ]; then
			echo "Ошибка обработки файла $log_file"
			continue
		fi
		echo "Файл $log_file содержит $lines строк с ключевым словом '$keyword'"
		line_counter=$((line_counter + lines))
	else
		echo "Файл $log_file не найден!
	fi
done

echo "С ключевым словом '$keyword' в лог-файлах найдено $line_counter строк"
