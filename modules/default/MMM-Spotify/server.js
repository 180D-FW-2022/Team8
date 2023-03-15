const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const { exec } = require('child_process');
const kill = require('kill-port');

const app = express();
const port = 8090;


app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.post('/submit', (req, res) => {
  const name = req.body.name;

  const data = {
    USERNAME: name,
    CLIENT_ID: "ea7f91ead4544cf88999efbcedf0ced0",
    CLIENT_SECRET: "19e6d25d90a14beeb1e91df7fca20ddf",
    TOKEN: `./${name}.json`
  };
//*TODO: CHANGE THIS TO ACTUAL FOLDER LOCATION *//
  fs.readFile('/Users/xuan-huongnguyen/Desktop/Team8/MagicMirror/modules/MMM-Spotify/spotify.config.json', 'utf8', (err, jsonString) => {
    if (err) {
      console.log('Error reading file:', err);
      res.status(500).send('Error reading file');
      return;
    }

    let configData = [];
    if (jsonString) {
      configData = JSON.parse(jsonString);
    }

    configData.push(data);
//*TODO: CHANGE THIS TO ACTUAL FOLDER LOCATION *//
    fs.writeFile('/Users/xuan-huongnguyen/Desktop/Team8/MagicMirror/modules/MMM-Spotify/spotify.config.json', JSON.stringify(configData), 'utf8', (err) => {
      if (err) {
        console.log('Error writing file:', err);
        res.status(500).send('Error writing file');
        return;
      }

      console.log('Data saved successfully');
      return true;
    
    });
  });
});


const server = app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

module.exports = app;
