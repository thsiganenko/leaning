module.exports = (list) => {
  list = list.map((user) => { return user.id; });
  return (users) => { return users.every((current) => { return list.indexOf(current.id) !== -1}); };
};
