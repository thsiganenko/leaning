var fs = require('fs');
var path = require('path');

var dir = process.argv[2];
var ext = process.argv[3] || 'js';
ext = '.' + ext;

if (dir === undefined) { 
  // TODO: Exit 
}

fs.readdir(dir, (err, list) => {
  list.filter((name) => { return path.extname(name) === ext;}).forEach((name) => { console.log(name);});
});
