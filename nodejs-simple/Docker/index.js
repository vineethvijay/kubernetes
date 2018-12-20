var express = require('express');

// Constants

var DEFAULT_PORT = 8080;
var PORT = process.env.PORT || DEFAULT_PORT;
var counter = 0;

var os = require("os");
var hostname = os.hostname();

// App
var app = express();
app.get('/', function (req, res) {
  counter += 1;
  res.send('Hello World -' + counter + '-' + hostname);
});

app.listen(PORT)
console.log('Running on http://localhost:' + PORT);