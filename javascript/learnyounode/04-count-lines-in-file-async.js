var fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    return console.log('error');
  }

  console.log(data.split('\n').length - 1);
});
