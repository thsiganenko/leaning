function duckTyping () {
  let count = 0;
  if (arguments.length === 0) return count;
  
  return Array.prototype.filter.call(arguments, (item) => { return Object.prototype.hasOwnProperty.call(item, 'quack'); }).length;
  
};

module.exports = duckTyping
