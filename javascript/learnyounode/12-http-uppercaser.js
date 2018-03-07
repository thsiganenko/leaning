var http = require('http');
var map = require('through2-map');

var server = http.createServer((request, response) => {
  if (request.method === 'POST') {
    request.setEncoding('utf8');
    request.on('data', (data) => {
      response.write(data.toUpperCase());
    });
  }
});

server.listen(process.argv[2]);
