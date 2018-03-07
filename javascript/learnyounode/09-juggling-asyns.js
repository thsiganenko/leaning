var http = require('http');

var responses = [];
var count = 0;

var output = (arr) => {
  arr.forEach((item) => { console.log(item); }); 
};

function getResponse(i) {
  http.get(process.argv[2+i], (data) => {
    let content = '';
    data.on('data', (chunck) => { content += chunck; });
    data.on('end', () => {
      responses[i] = content;
      count++;
      if (count === process.argv.length - 2) {
        output(responses); 
      }
    });
  });
}

for (var i = 0, len = process.argv.length - 2; i < len; i++) {
  getResponse(i);
}
