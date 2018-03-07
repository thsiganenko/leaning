function romanToArab(roman) {
    /* Функция принимает число, в Римской записи и возвращает целое число
     *
     * @param roman: str число в Римской записи
     * @return: int целое число
     */
    var romanToArab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};
    var result = 0;

    for (var i = 0; i < roman.length; i++) {
        if (romanToArab[roman[i]] > romanToArab[roman[i-1]]) {
            result += romanToArab[roman[i]] - romanToArab[roman[i-1]] * 2;
        } else {
            result += romanToArab[roman[i]];
        }
    }
    return result;
}
