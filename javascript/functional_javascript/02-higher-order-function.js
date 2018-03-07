var counter = (operation, num) => {
  if (num > 0) {
    counter(operation, num - 1);
  }
  return operation();
};

module.exports = counter
