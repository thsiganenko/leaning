var http = require('http');
var url = require('url');

var server = http.createServer((request, response) => {
  response.writeHead(200, { 'content-type' : 'application/json' });
  let reqURL = url.parse(request.url, true);
  
  if (reqURL.pathname === '/api/parsetime') {
    let date = new Date(reqURL.query.iso);
    let time = {
      'hour': date.getHours(),
      'minute': date.getMinutes(),
      'second': date.getSeconds()
    };
    response.end(JSON.stringify(time));
    
  } else if (reqURL.pathname === '/api/unixtime') {
    let date = new Date(reqURL.query.iso);
    response.end(JSON.stringify({'unixtime': date.getTime()}));
  } else {

    response.write('I don\'t understand'); 
  }
});

server.listen(process.argv[2]);
