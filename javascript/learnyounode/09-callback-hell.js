var http = require('http');

var url1 = process.argv[2];
var url2 = process.argv[3];
var url3 = process.argv[4];

http.get(url1, (response) => {
  let content = '';
  response.setEncoding('utf8');
  response.on('data', (data) => { content += data; });
  response.on('end', () => {
    console.log(content);
    http.get(url2, (response) => {
      let content = '';
      response.setEncoding('utf8');
      response.on('data', (data) => { content += data; });
      response.on('end', () => {
        console.log(content);
        http.get(url3, (response) => {
          let content = '';
          response.setEncoding('utf8');
          response.on('data', (data) => { content += data; });
          response.on('end', () => {
            console.log(content);
          });
        });
      });
    });
  });
});
