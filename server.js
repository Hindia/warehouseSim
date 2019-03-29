//server.js
const express = require('express');
const favicon = require('express-favicon');
const path = require('path');
const port = process.env.PORT || 8080;
const app = express();
app.use(favicon(warehouseSim + '/build/favicon.ico'));
// the __dirname is the current directory from where the script is running
app.use(express.static(warehouseSim));
//static file declaration
app.use(express.static(path.join(warehouseSim, 'build')));

//build mode
app.get('*', function (req, res) {
  res.sendFile(path.join(warehouseSim, 'build', 'index.html'));
});

app.listen(port);