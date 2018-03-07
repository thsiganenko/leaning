var recursion = (arr, func, init) => {
  if (arr.length === 0) {
    return init;
  }
  var temp = arr.slice();
  var cur = temp.pop();
  return func(recursion(temp, func, init), cur, temp.length, arr);
};

module.exports = recursion;
