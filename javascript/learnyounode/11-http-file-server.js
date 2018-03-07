var http = require('http');
var fs = require('fs');

var server = http.createServer((request, response) => {
  let stream = fs.createReadStream(process.argv[3]);
  response.writeHead(200, { 'content-type': 'text/plain' });
  stream.pipe(response);
});

server.listen(process.argv[2]);
