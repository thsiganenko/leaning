var http = require('http');

var url = process.argv[2];

http.get(url, (response) => {
  let content = '';
  response.setEncoding('utf8');
  response.on('data', (data) => { content += data; });
  response.on('end', () => {
    console.log(content.length);
    console.log(content);
  });
  
});
