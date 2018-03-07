// Подключаем библиотеку для работы с файловой системой
var fs = require('fs');
// Читаем имя файла из параметров командной строки
var fileName = process.argv[2];

// Проверяем, было ли передано имя файла
if (!fileName) {
	console.log('Requere file name!');
	// TODO: Скрипт должен завершить работу
}

// Читаем файл в буфер
var buffer = fs.readFileSync(fileName);
// Конвертируем буфер в строку
// Разбивает текст на строки по \n
// Получаем длину и отбрасываем последнюю пустую строку
console.log(buffer.toString().split('\n').length - 1);
