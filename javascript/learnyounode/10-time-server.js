var net = require('net');

var server = new net.createServer((socket) => {
  let date = new Date();
  
  let year = date.getFullYear();
  let month = '' + (1 + +date.getMonth());
  let day = date.getDate();
  let hours = date.getHours();
  let minutes = date.getMinutes();
  
  let output = '';
  
  output +=  year + '-';
  output += (month.length < 2) ? '0' + month : month;
  output += '-' + ((day.length < 2) ? '0' + day : day);
  output += ' ' + ((hours.length < 2) ? '0' + hours : hours);
  output += ':' + ((minutes.length < 2) ? '0' + minutes : minutes);
  
  socket.end(output + '\n');
});

server.listen(process.argv[2]);
