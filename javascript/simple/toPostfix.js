function toPostfix(infix) {
    /* Функция принимает строку с записью выражения в инфиксной нотации и
     * возвращает строку в постфиксной нотации
     */
    var stack = [];
    var result = '';
    var prior = { '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3 };
    var flag = false;

    for (var i = 0; i < infix.length; i++) {
        if (/\d/.test(infix[i])) {
            if (flag) {
                result += ' ' + infix[i];
                flag = false;
            } else {
                result += infix[i];
            }
        } else if (infix[i] === '(') {
            stack.push(infix[i]);
            flag = true;
        } else if (stack.length === 0) {
            stack.push(infix[i]);
            flag = true;
        } else if (prior[stack[stack.length - 1]] < prior[infix[i]]) {
            stack.push(infix[i]);
            flag = true;
        } else if (infix[i] === ')') {
            while (stack.length > 0 && stack[stack.length - 1] !== '(') {
                result += stack.pop();
            }
            stack.pop();
            flag = true;
        } else {
            while (stack.length > 0 && prior[stack[stack.length - 1]] >= prior[infix[i]]) {
                result += stack.pop();
            }
            stack.push(infix[i]);
            flag = true;
        }
    }
    while (stack.length !== 0) {
        result += stack.pop();
    }
    return result.trim();
}
