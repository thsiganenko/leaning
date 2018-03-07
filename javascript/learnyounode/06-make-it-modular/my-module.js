var fs = require('fs');
var path = require('path');

module.exports = (dir, ext, callback) => {
  fs.readdir(dir, (err, list) => {
    if (err) {
      return callback(err);
    }

    ext = '.' + ext;

    list = list.filter((name) => { return path.extname(name) === ext; });

    return callback(null, list);
  });
}

