var filterDirList = require('./my-module.js');

dir = process.argv[2];
ext = process.argv[3];

filterDirList(dir, ext, (err, list) => {
  if (err) {
    return console.error('Error!', err);
  }
  list.forEach((name) => { console.log(name); });
});
