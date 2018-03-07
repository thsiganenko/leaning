module.exports = (arr) => {
  return arr.filter((obj) => { return obj.message.length < 50; }).map((obj) => { return obj.message; });
}
