module.exports = (arr) => {
  return arr.reduce((obj, item) => {
    if (obj[item] === undefined) obj[item] = 0;
    obj[item] += 1;
    return obj;
  }, {});
};
